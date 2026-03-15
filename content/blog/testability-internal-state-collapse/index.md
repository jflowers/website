---
title: "Testability: Internal State Collapse"
date: "2005-10-09"
draft: false
categories:
  - "Uncategorized"
aliases:
  - "/WordPress/?p=40"
  - "/WordPress/index.php?p=40"
params:
  wayback_url: "https://web.archive.org/web/20070307194606/http://jayflowers.com:80/WordPress/?p=40"
  original_url: "http://jayflowers.com:80/WordPress/?p=40"
  archived_from: Wayback Machine

---

## Testability: Internal State Collapse

So I have started research for a book that I would like to write.  I am currently looking for  a metric or metric that will indicate when a design is not very testable.  I came across an interesting concept, internal state collapse.  This is where the input parameters are not released from the member.  For example:


```csharp
public interface IWarehouse

{

    bool HasInventory(InventoryItem inventoryItem, int amount);

    void Remove(InventoryItem inventoryItem, int amount);

    void Add(InventoryItem inventoryItem, int amount);

}
```

The members Add and Remove do not release amount or inventoryItem.  This is known as internal state collapse.  The interest here is that it is very difficult to test.  Lets examine this a little closer.


```csharp
public void Add(InventoryItem inventoryItem, int amount)

{

    if (this.HasInventory(inventoryItem, amount))

    {

        this.Inventory[inventoryItem] = (int) this.Inventory[inventoryItem] + amount;

    }
```

    else


```csharp
    {

        this.Inventory[inventoryItem] = amount;

    }

}
```

No surprises there.  Some people might say “well just use HasInventory to verify that Add was successful”.  This is fine in production code but test code should try not to use production code to verify production code.  What if there was a bug in HasInventory?  When trying to test Add I don’t want to get sidetracked by a bug elsewhere in the product.  So the problem is that the information needed for verification is not accessible or in other cases has vanished.  After more research I found an answer:


```csharp
public void Add(InventoryItem inventoryItem, int amount)

{

    if (this.HasInventory(inventoryItem, amount))

    {

        this.Inventory[inventoryItem] = (int) this.Inventory[inventoryItem] + amount;

        System.Diagnostics.Debug.Assert(this.Inventory[inventoryItem] > amount, “The inventory should be more than the amount that was just added.”);

    }
```

    else


```csharp
    {

        this.Inventory[inventoryItem] = amount;

        System.Diagnostics.Debug.Assert(this.Inventory[inventoryItem] == amount, “The inventory should be that same as what was just added.”);

    }

}
```

This feels a lot like a stint to me.  The assertions act as stints allowing the verification while maintaining encapsulation.  I have seen other solutions that offer information through public members that are conditionally compiled (i.e. encapsulation is only broken for testing).  Any kind of solution that breaks the rules just to achieve testability is a lazy solution in my book (that is the bad kind not the good kind of lazy).  I doubt that the inventors and practitioners of those solutions hold OOP values and principles.  They certainly are not practising them.

Anyway I hope to have the time to finish up the research into testability metrics here in the next two weeks.  If you are interested in this kind of thing you can keep track of my progress in more detail at [JayFlowers.com](http://jayflowers.com/).
