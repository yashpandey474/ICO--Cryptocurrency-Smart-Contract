//TITLE: YASHCOINS ICO


//VERSION OF COMPILER
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

//CREATE A SMART CONTRACT
contract yashcoin_ico{

    //DEFINITION OF SMART CONTRACT

/*PUBLIC VARIABLES: CAN BE ACCESSED EVEN OUTSIDE OF CONTRACT*/
//UINT->UNSIGNED INTEGER [POSITIVE]
    
    /*INTRODDUCING MAXIMUM NUMBER OF YASHCOINS FOR SALE*/
    uint public max_yashcoins = 1000000;

    /*INTRODUCING THE USD TO YASHCOINS CONVERSION RATE */
    uint public usd_to_yashcoins = 1000;
    
    /*INTRODUCING TOTAL NUMBER OF YASHCOINS THAT HAVE BEEN BOUGHT*/
    uint public total_yashcoins_bought = 0;

    //MAPPING FROM THE INVESTOR ADDRESS TO ITS EQUITY IN YASHCOINS AND USD
    //-> A mapping is a function but data is stored in array
    //-> Returns result for all inputs [address => equity]
    //-> mapping (initial_dtype => final_dtype) name_of_output_var
    mapping(address => uint) equity_yashcoins;
    mapping(address => uint) equity_usd;

    //MODIFIER TO CHECK IF INVESTOR CAN BUY YASHCOINS OR NOT [ANY MORE LEFT]
    //-> modifier name_of_modifier()
    modifier can_buy_yashcoins(uint usd_invested){
        //CONDITION
        require(usd_invested * usd_to_yashcoins + total_yashcoins_bought <= max_yashcoins);
        _; //FUNCTIONS LINKED TO MODIFIER ONLY APPLIED IF REQUIRE CONDITION IS TRUE
    }

    //->GETTING THE EQUITY IN YASHCOINS: external constant-> doens't vary and outside of contract's scope
    function equity_in_yashcoin(address investor) external view returns (uint){
        //USE THE MAPPING
        return equity_yashcoins[investor];
    }

    //->GETTING THE EQUITY IN USD
    function equity_in_usd(address investor) external view returns (uint){
        //USE THE MAPPING
        return equity_usd[investor];
    }
    
    //-> BUYING YASHCOINSL: usd_invested to buy yashcoins
    function buy_yashcoins(address investor, uint usd_invested) external
    can_buy_yashcoins(usd_invested) {

        uint yashcoins_bought  = usd_invested * usd_to_yashcoins;

        //UPDATE EQUITY
        equity_yashcoins[investor] += usd_invested * usd_to_yashcoins;
        equity_usd[investor] = equity_yashcoins[investor] / usd_to_yashcoins;

        //UPDATE TOTAL BOUGHT
        total_yashcoins_bought += yashcoins_bought;
    }

    //-> SELLING YASHCOINS; number of coins to sell
    function sell_yashcoins(address investor, uint yashcoins_to_sell) external {

        //UPDATE EQUITY
        equity_yashcoins[investor] -= yashcoins_to_sell;
        equity_usd[investor] = equity_yashcoins[investor] / usd_to_yashcoins;

        //UPDATE TOTAL BOUGHT
        total_yashcoins_bought -= yashcoins_to_sell;
    }
}
