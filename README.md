## Price elasticity
Author: Valéria Custódio

Date: 22nd September 2023
## Business problem
B&H Photo Video is an American retailer specializing in photography and videography that operates primarily through online e-commerce.
In a biannual meeting, the Chief Financial Officer (CFO) has set forth an objective to enhance B&H’s sponsorship and fellowship programs at BRIC, Brooklyn's largest presenter of free cultural events. To attain this goal, the company intends to forecast the revenue for a campaign that involves offering a 10% discount on its mirrorless cameras. 
To address this objective, the CFO has posed two questions:
  1.	Which mirrorless camera should the discount be applied to optimize revenue?
  2.	What are the anticipated revenue figures?
## Solution
For this problem, I will calculate the price elasticity of the products in the mirrorless camera category at B&H Photo Video. The solution's planning involved applying the SAPE method developed by the Comunidade DS. This method encompasses the definition of an output (SA: saida), the process (P) and the input (E: entrada). Moreover, the project will be executed in accordance with the Cross-Industry Standard Process for Data Science (CRISP-DS) methodology. This methodology is characterized by a cyclical approach across the various analysis phases, designed to continually enhance the value to the business. Upon delivering the initial set of solutions, the process can be iterated to discover new insights, fine-tune parameters, improve accuracy, and increase the value delivered to the business.
## Planning (SAPE and CRISP-DS method)
#### 1.	Output (Saida)
     
  A Streamlit app with mirrorless camera products with the respective price elasticity and the anticipated revenue figures for each product.
  
#### 2.	Process (CRISP-DS method)

  Step01: Define the problem

  Step02: Understand the root of the problem
  
  Step03: Data collection
  
  Step04: Data description
  
  Step05: Exploratory data analysis (EDA)
  
  Step06: Feature Engineering
  
  Step07: Data description of the newly generated dataset
  
  Step08: EDA on the new dataset
  
  Step09: Machine learning algorithm
  
  Step10: Price elasticity calculation
  
  Step11: Business Performance
  
#### 3.Input (Entrada)
     
  A csv file with all the products sold at B&H Photo Video.
## Results
-	B&H has products that can be grouped into 51 categories. The category mirrorless camera is the category that generates the highest sales at B&H Photo Video
-	December is the month that the store experiences the highest sales
-	The category mirrorless camera has 13 products from different brands, where Canon - EOS Rebel SL2 DSLR Camera Body Deluxe Kit and Panasonic – Lumix G85 Mirrorless Camera with 12-60mm Lens – Black presents showed statistically significant price elasticity, 90.152765 and -98.229486, respectively.
-	The revenue for the Canon - EOS Rebel SL2 DSLR Camera Body Deluxe Kit and Panasonic - Lumix G85 Mirrorless Camera with 12-60mm Lens – Black stand at $9402.24 and $14876.1, respectively.
-	Implementing the 10% reduction in prices and with the expected increase in demand, the anticipated revenue figures are $76287.38 and $116638.35, for the Canon - EOS Rebel SL2 DSLR Camera Body Deluxe Kit and Panasonic - Lumix G85 Mirrorless Camera with 12-60mm Lens – Black, respectively.
## Conclusions
The price elasticity analysis of the products in the mirrorless camera category in B&H Photo and Video shows that from 13 products in this category, the Canon - EOS Rebel SL2 DSLR Camera Body Deluxe Kit and Panasonic - Lumix G85 Mirrorless Camera with 12-60mm Lens – Black  have statistically significant price elasticity. They present an elastic demand, meaning that they are highly responsive to changes in its price.

Before performing this project,  we found that for the  camera EOS Rebel SL2 DSLR Camera Body Deluxe Kit,  the current revenue stands at $9402.24. If we implement a suggested 10% price reduction, the revenue would decrease to $ 8462.02, resulting in an initial reduction of $940.22. However, using the price elasticity calculated in this project, this price reduction is expected to stimulate an increase in demand. As a result, the projected revenue would surge to $76287.38. This substantial uptick represents an impressive revenue increase of $66885.14 or a remarkable growth rate of 711.37 %. Similarly, in Panasonic - Lumix G85 Mirrorless Camera with 12-60mm Lens - Black, the current revenue stands at $14876.1. If we implement a suggested 10% price reduction, the revenue would decrease to $ 13388.49, resulting in an initial reduction of $1487.61. Applying the price elasticity calculated in this project, the projected revenue would surge to $ 131514.45, representing an impressive revenue increase of $116638.35 or a remarkable growth rate of 784.07 %. 

By combining the revenue for these two products, the total projected revenue for this campaign will be $183523.49.

## Future perspectives
-	Calculate the Cross-Price Elasticity, which measures how the quantity demanded from one product responds to changes in the price of the other products.
-	Improve the README file
-	Prepare the app on Streamlit
## Acknowledgement
To Comunidade DS for making possible the elaboration of this project. To Alexsandro Silveira for the amazing lecture on price elasticity and all the processes to develop this project. To Meigarom Lopes for creating this community and for letting us pick his mind on this Data Science universe. 
