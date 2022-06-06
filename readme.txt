CANDLE ARTIST APP

OBJECTIVE:

Automate the process of paying out artists, which should happen quarterly if possible, but is currently happening
twice yearly. The process currently happens like this:

    1. Artists receive an order
    2. Total sales are tallied at the end of the quarter per artist
    3. An artist cut is taken of net sales - this varies by artist. It is anywhere from 0 to 17.5% to 20%.
    4. Deductions are made for:
        a. Cost of blanks
        b. Cost of printing/ink
        c. Cost of pick/pack
    5. The artist is paid out via PayPal.

IDEA:

Create a Shopify app which automates this process. It might work like this:

    1. Shopify receives an order.
    2. Each item in the order is logged by the app. Individual items are identified via Shopify "Item Type"
    3. Each individual record is logged to a Pandas dataframe. Each artist has a CSV which Pandas updates using this
       dataframe.
    4. This CSV receives the following information about an order via metafields. Each SKU is updated with these fields
       during SKU creation, or business rules can be created which send appropriate metafields in ChAd.
        a. Cost of blank
        b. Cost of print/ink
        c. Cost of pick/pack
        d. Artist cut percentage (can be set at a collection level)
    5. The following cells are also created -
        a. Cell which calculates the Artist payout
        b. Cell which calculates the total deduction per SKU
        c. Cell which calculates the Candle cut
        d. Cell which calculates the total deductions
    6. These CSVs are all emailed quarterly.

similar app:
https://apps.shopify.com/vendor-payout#reviews

follow this tutorial:
https://www.youtube.com/watch?v=CbsbunnH8Q0
https://www.youtube.com/watch?v=PBRMvAKz_rQ
https://www.youtube.com/watch?v=CnCBbiLw-HU