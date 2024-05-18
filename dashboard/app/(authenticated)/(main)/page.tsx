import { Button } from "@/components/ui/button";
import * as React from "react";
import { XIcon } from "lucide-react";
import {
  ClosableDiv,
  ClosableDivProvider,
  CloseBtn,
} from "@/components/headless/ClosableDiv";
import { HeaderShell } from "@/components/domain/HeaderShell";
import { Search } from "./_parts/Search";
import { Link } from "@/lib/router-events";
import { CopilotsContainer } from "./_parts/CopilotsContainer";

export default async function HomePage() {
  return (
    <div className="flex h-full w-full flex-col overflow-hidden">
      <HeaderShell>
        <div className="flex flex-1 items-center justify-between">
          <div>
            <h1 className="text-lg font-bold text-accent-foreground">
            Cusmato Copilots ✨
            </h1>
          </div>
          <div className="space-x-2">
            <Button asChild>
              <Link href="/create/copilot">Create Cusmato Assistant</Link>
            </Button>
          </div>
        </div>
      </HeaderShell>

      <div className="flex-1 overflow-auto p-8 pt-4">
        <ClosableDivProvider>
          <ClosableDiv className="group relative mb-2 w-full overflow-hidden rounded-lg bg-primary/20 px-8 py-6 before:absolute before:-bottom-5 before:right-14 before:-z-10 before:aspect-square before:h-full before:w-auto before:-rotate-45 before:bg-[url('/rocket_silver.svg')] before:bg-no-repeat before:opacity-60">
            <div className="flex items-center justify-between gap-5">
              </div>
              <div>
                <h1 className="text-lg font-bold text-accent-foreground">
                  Learn Cusmato with video tutorials
                </h1>
            </div>
            <CloseBtn className="absolute -right-1 -top-1 rounded-full border border-border bg-white p-1 opacity-0 shadow group-hover:opacity-100 ">
              <XIcon className="h-4 w-4" />
            </CloseBtn>
          </ClosableDiv>
        </ClosableDivProvider>
        <Search />
        <CopilotsContainer />
      </div>
    </div>
  );
}
