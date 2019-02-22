# -*- coding: utf-8 -*-
'''
>>> from opem.Dynamic.Padulles2 import *
>>> import shutil
>>> Test_Vector={"T":343,"E0":0.6,"N0":5,"KO2":0.0000211,"KH2":0.0000422,"KH2O":0.000007716,"tH2":3.37,"tO2":6.74,"tH2O":18.418,"B":0.04777,"C":0.0136,"Rint":0.00303,"rho":1.168,"qH2":0.0004,"i-start":0.1,"i-stop":4,"i-step":0.1,"Name":"test3"}
>>> Padulles_II_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Padulles-II-Model Simulation
###########
Analyzing . . .
I : 0.1
E : 3.0120122442199793 V
FC Efficiency : 0.4265389961269225
FC Power : 0.33270041697899955 W
FC Voltage : 3.3270041697899955 V
PH2 : 2.169018669476965 atm
PH2O : 2.669687710942903 atm
PO2 : 2.09696938340326 atm
Power-Thermal : 0.2822995830210005 W
###########
I : 0.2
E : 3.012012104448671 V
FC Efficiency : 0.42225504989786394
FC Power : 0.6587178778406679 W
FC Voltage : 3.293589389203339 V
PH2 : 2.1690046190953503 atm
PH2O : 2.6696704173475743 atm
PO2 : 2.0969614505650616 atm
Power-Thermal : 0.5712821221593323 W
###########
I : 0.3
E : 3.0120119646768333 V
FC Efficiency : 0.4197329719509197
FC Power : 0.9821751543651522 W
FC Voltage : 3.273917181217174 V
PH2 : 2.1689905687137356 atm
PH2O : 2.669653123752246 atm
PO2 : 2.0969535177268637 atm
Power-Thermal : 0.8628248456348478 W
###########
I : 0.4
E : 3.0120118249044676 V
FC Efficiency : 0.41793223959535725
FC Power : 1.3039485875375147 W
FC Voltage : 3.259871468843787 V
PH2 : 2.1689765183321215 atm
PH2O : 2.6696358301569174 atm
PO2 : 2.0969455848886653 atm
Power-Thermal : 1.1560514124624854 W
###########
I : 0.5
E : 3.0120116851315726 V
FC Efficiency : 0.41652676431084773
FC Power : 1.6244543808123062 W
FC Voltage : 3.2489087616246124 V
PH2 : 2.1689624679505073 atm
PH2O : 2.669618536561589 atm
PO2 : 2.096937652050467 atm
Power-Thermal : 1.450545619187694 W
###########
I : 0.6
E : 3.012011545358149 V
FC Efficiency : 0.4153712975747617
FC Power : 1.943937672649885 W
FC Voltage : 3.2398961210831416 V
PH2 : 2.1689484175688927 atm
PH2O : 2.6696012429662606 atm
PO2 : 2.0969297192122687 atm
Power-Thermal : 1.7460623273501152 W
###########
I : 0.7
E : 3.0120114055841967 V
FC Efficiency : 0.4143883594017745
FC Power : 2.2625604423336885 W
FC Voltage : 3.232229203333841 V
PH2 : 2.1689343671872785 atm
PH2O : 2.669583949370932 atm
PO2 : 2.0969217863740703 atm
Power-Thermal : 2.0424395576663112 W
###########
I : 0.8
E : 3.0120112658097153 V
FC Efficiency : 0.4135317011453444
FC Power : 2.580437815146949 W
FC Voltage : 3.225547268933686 V
PH2 : 2.168920316805664 atm
PH2O : 2.6695666557756033 atm
PO2 : 2.096913853535872 atm
Power-Thermal : 2.3395621848530515 W
###########
I : 0.9
E : 3.0120111260347056 V
FC Efficiency : 0.41277149148017567
FC Power : 2.897655870190834 W
FC Voltage : 3.219617633545371 V
PH2 : 2.1689062664240497 atm
PH2O : 2.6695493621802746 atm
PO2 : 2.0969059206976737 atm
Power-Thermal : 2.6373441298091667 W
###########
I : 1.0
E : 3.0120109862591664 V
FC Efficiency : 0.4120873617867766
FC Power : 3.2142814219368576 W
FC Voltage : 3.2142814219368576 V
PH2 : 2.168892216042435 atm
PH2O : 2.669532068584946 atm
PO2 : 2.0968979878594753 atm
Power-Thermal : 2.9357185780631427 W
###########
I : 1.1
E : 3.0120108464830992 V
FC Efficiency : 0.4114647839578894
FC Power : 3.5303678463586916 W
FC Voltage : 3.2094253148715377 V
PH2 : 2.168878165660821 atm
PH2O : 2.6695147749896178 atm
PO2 : 2.096890055021277 atm
Power-Thermal : 3.234632153641309 W
###########
I : 1.2
E : 3.0120107067065027 V
FC Efficiency : 0.41089303097642904
FC Power : 3.845958769939376 W
FC Voltage : 3.2049656416161465 V
PH2 : 2.1688641152792063 atm
PH2O : 2.669497481394289 atm
PO2 : 2.0968821221830787 atm
Power-Thermal : 3.5340412300606245 W
###########
I : 1.3
E : 3.0120105669293777 V
FC Efficiency : 0.4103639566273662
FC Power : 4.161090520201494 W
FC Voltage : 3.2008388616934567 V
PH2 : 2.168850064897592 atm
PH2O : 2.669480187798961 atm
PO2 : 2.0968741893448803 atm
Power-Thermal : 3.833909479798507 W
###########
I : 1.4
E : 3.012010427151724 V
FC Efficiency : 0.40987122872897686
FC Power : 4.475793817720427 W
FC Voltage : 3.1969955840860194 V
PH2 : 2.168836014515978 atm
PH2O : 2.6694628942036323 atm
PO2 : 2.096866256506682 atm
Power-Thermal : 4.1342061822795735 W
###########
I : 1.5
E : 3.012010287373541 V
FC Efficiency : 0.409409827543193
FC Power : 4.790094982255358 W
FC Voltage : 3.1933966548369055 V
PH2 : 2.1688219641343633 atm
PH2O : 2.6694456006083036 atm
PO2 : 2.0968583236684837 atm
Power-Thermal : 4.434905017744642 W
###########
I : 1.6
E : 3.0120101475948298 V
FC Efficiency : 0.40897570639787845
FC Power : 5.104016815845523 W
FC Voltage : 3.190010509903452 V
PH2 : 2.1688079137527487 atm
PH2O : 2.669428307012975 atm
PO2 : 2.096850390830286 atm
Power-Thermal : 4.7359831841544775 W
###########
I : 1.7
E : 3.012010007815589 V
FC Efficiency : 0.4085655553769282
FC Power : 5.417579264298068 W
FC Voltage : 3.18681133194004 V
PH2 : 2.1687938633711346 atm
PH2O : 2.6694110134176463 atm
PO2 : 2.0968424579920875 atm
Power-Thermal : 5.037420735701932 W
###########
I : 1.8
E : 3.01200986803582 V
FC Efficiency : 0.40817663265783805
FC Power : 5.730799922516047 W
FC Voltage : 3.183777734731137 V
PH2 : 2.16877981298952 atm
PH2O : 2.6693937198223177 atm
PO2 : 2.096834525153889 atm
Power-Thermal : 5.339200077483954 W
###########
I : 1.9
E : 3.012009728255522 V
FC Efficiency : 0.4078066415116356
FC Power : 6.04369442720244 W
FC Voltage : 3.180891803790758 V
PH2 : 2.1687657626079058 atm
PH2O : 2.669376426226989 atm
PO2 : 2.096826592315691 atm
Power-Thermal : 5.6413055727975605 W
###########
I : 2.0
E : 3.012009588474695 V
FC Efficiency : 0.40745363888936376
FC Power : 6.356276766674075 W
FC Voltage : 3.1781383833370374 V
PH2 : 2.168751712226291 atm
PH2O : 2.669359132631661 atm
PO2 : 2.0968186594774925 atm
Power-Thermal : 5.943723233325926 W
###########
I : 2.1
E : 3.0120094486933398 V
FC Efficiency : 0.40711596633503955
FC Power : 6.668559528567949 W
FC Voltage : 3.1755045374133086 V
PH2 : 2.168737661844677 atm
PH2O : 2.669341839036332 atm
PO2 : 2.096810726639294 atm
Power-Thermal : 6.246440471432053 W
###########
I : 2.2
E : 3.0120093089114555 V
FC Efficiency : 0.4067921969851981
FC Power : 6.980554100266 W
FC Voltage : 3.172979136484545 V
PH2 : 2.168723611463063 atm
PH2O : 2.669324545441004 atm
PO2 : 2.096802793801096 atm
Power-Thermal : 6.5494458997340015 W
###########
I : 2.3
E : 3.012009169129042 V
FC Efficiency : 0.4064810943595029
FC Power : 7.292270832809483 W
FC Voltage : 3.170552536004123 V
PH2 : 2.168709561081448 atm
PH2O : 2.6693072518456753 atm
PO2 : 2.0967948609628975 atm
Power-Thermal : 6.8527291671905175 W
###########
I : 2.4
E : 3.0120090293460997 V
FC Efficiency : 0.40618157992825576
FC Power : 7.603719176256948 W
FC Voltage : 3.168216323440395 V
PH2 : 2.168695510699834 atm
PH2O : 2.6692899582503467 atm
PO2 : 2.096786928124699 atm
Power-Thermal : 7.156280823743052 W
###########
I : 2.5
E : 3.0120088895626287 V
FC Efficiency : 0.40589270730496035
FC Power : 7.914907792446728 W
FC Voltage : 3.1659631169786913 V
PH2 : 2.1686814603182194 atm
PH2O : 2.669272664655018 atm
PO2 : 2.096778995286501 atm
Power-Thermal : 7.460092207553273 W
###########
I : 2.6
E : 3.0120087497786283 V
FC Efficiency : 0.40561364150350754
FC Power : 8.225844649691133 W
FC Voltage : 3.163786403727359 V
PH2 : 2.168667409936605 atm
PH2O : 2.6692553710596894 atm
PO2 : 2.0967710624483025 atm
Power-Thermal : 7.764155350308868 W
###########
I : 2.7
E : 3.0120086099941004 V
FC Efficiency : 0.405343642112191
FC Power : 8.536537102882745 W
FC Voltage : 3.1616804084750902 V
PH2 : 2.1686533595549906 atm
PH2O : 2.6692380774643607 atm
PO2 : 2.096763129610104 atm
Power-Thermal : 8.068462897117257 W
###########
I : 2.8
E : 3.0120084702090426 V
FC Efficiency : 0.4050820495292294
FC Power : 8.84699196171837 W
FC Voltage : 3.1596399863279894 V
PH2 : 2.168639309173376 atm
PH2O : 2.6692207838690325 atm
PO2 : 2.096755196771906 atm
Power-Thermal : 8.37300803828163 W
###########
I : 2.9
E : 3.0120083304234564 V
FC Efficiency : 0.404828273614746
FC Power : 9.157215549165555 W
FC Voltage : 3.1576605341950192 V
PH2 : 2.168625258791762 atm
PH2O : 2.669203490273704 atm
PO2 : 2.0967472639337075 atm
Power-Thermal : 8.677784450834444 W
###########
I : 3.0
E : 3.012008190637341 V
FC Efficiency : 0.40458178426735336
FC Power : 9.467213751856068 W
FC Voltage : 3.1557379172853564 V
PH2 : 2.1686112084101477 atm
PH2O : 2.6691861966783756 atm
PO2 : 2.0967393310955096 atm
Power-Thermal : 8.982786248143931 W
###########
I : 3.1
E : 3.0120080508506963 V
FC Efficiency : 0.4043421035464688
FC Power : 9.776992063753617 W
FC Voltage : 3.1538684076624572 V
PH2 : 2.168597158028533 atm
PH2O : 2.669168903083047 atm
PO2 : 2.0967313982573113 atm
Power-Thermal : 9.288007936246384 W
###########
I : 3.2
E : 3.0120079110635234 V
FC Efficiency : 0.40410879904574315
FC Power : 10.08655562418175 W
FC Voltage : 3.152048632556797 V
PH2 : 2.168583107646919 atm
PH2O : 2.6691516094877183 atm
PO2 : 2.096723465419113 atm
Power-Thermal : 9.593444375818251 W
###########
I : 3.3
E : 3.0120077712758215 V
FC Efficiency : 0.40388147828648513
FC Power : 10.395909251094128 W
FC Voltage : 3.1502755306345844 V
PH2 : 2.1685690572653042 atm
PH2O : 2.6691343158923897 atm
PO2 : 2.0967155325809146 atm
Power-Thermal : 9.899090748905872 W
###########
I : 3.4
E : 3.0120076314875908 V
FC Efficiency : 0.403659783948294
FC Power : 10.705057470308757 W
FC Voltage : 3.1485463147966937 V
PH2 : 2.16855500688369 atm
PH2O : 2.669117022297061 atm
PO2 : 2.0967075997427163 atm
Power-Thermal : 10.204942529691243 W
###########
I : 3.5
E : 3.012007491698831 V
FC Efficiency : 0.4034433897912177
FC Power : 11.014004541300244 W
FC Voltage : 3.1468584403714983 V
PH2 : 2.1685409565020755 atm
PH2O : 2.6690997287017324 atm
PO2 : 2.096699666904518 atm
Power-Thermal : 10.510995458699757 W
###########
I : 3.6
E : 3.0120073519095425 V
FC Efficiency : 0.4032319971525013
FC Power : 11.322754480042237 W
FC Voltage : 3.1452095777895104 V
PH2 : 2.168526906120461 atm
PH2O : 2.669082435106404 atm
PO2 : 2.0966917340663196 atm
Power-Thermal : 10.817245519957764 W
###########
I : 3.7
E : 3.012007212119725 V
FC Efficiency : 0.40302533192342654
FC Power : 11.631311079310091 W
FC Voltage : 3.1435975890027272 V
PH2 : 2.1685128557388467 atm
PH2O : 2.6690651415110755 atm
PO2 : 2.0966838012281213 atm
Power-Thermal : 11.123688920689911 W
###########
I : 3.8
E : 3.0120070723293786 V
FC Efficiency : 0.402823141929393
FC Power : 11.939677926787208 W
FC Voltage : 3.1420205070492657 V
PH2 : 2.168498805357232 atm
PH2O : 2.669047847915747 atm
PO2 : 2.096675868389923 atm
Power-Thermal : 11.43032207321279 W
###########
I : 3.9
E : 3.0120069325385037 V
FC Efficiency : 0.4026251946503726
FC Power : 12.247858421264336 W
FC Voltage : 3.140476518272907 V
PH2 : 2.168484754975618 atm
PH2O : 2.6690305543204187 atm
PO2 : 2.0966679355517246 atm
Power-Thermal : 11.737141578735665 W
###########
Report is generating ...
Done!
>>> Enernst_Calc(E0=None,N0=0,T=1, PH2=2.1, PO2=2.1,PH2O=2.1)
[Error] Enernst Calculation Failed (E0:None, N0:0, T:1, PH2:2.1, PO2:2.1, PH2O:2.1)
>>> PH2O_Calc(KH2O=None,tH2O=1,Kr=0.3,I=3,qH2O=0.3)
[Error] PH2O Calculation Failed (KH2O:None, tH2O:1, Kr:0.3, I:3, qH2O:0.3)
>>> Padulles_II_Data=Dynamic_Analysis(InputMethod={}, TestMode=True,PrintMode=False)
>>> Padulles_II_Data["Status"]
False
>>> shutil.rmtree("Padulles-II")

'''
