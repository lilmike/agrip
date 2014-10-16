Reference Information
=====================

This part of the manual provides detailed technical and summary
information that can be used by players to refer back to various
important points, without having to read through the main text again.

Key to the AudioQuake Sounds
----------------------------

This appendix is a list of the sounds AudioQuake uses to tell you what's
going on. It contains links to the sounds and descriptions of them.
Additionally, it gives you an example or two of when you'll hear the
sounds.

Depending on how your browser is set up, you should be able to listen to
these sounds quite easily whilst reading the book (tell your browser to
open them with a program that can play WAVE files and also tell it to do
this automatically for all WAVE files).

**Note:** Many in-game events are spoken to you so you won't find them
included in this list. Also, some of the sounds we use are in the Quake
data files and as such cannot be included here because we don't own the
copyright on the Quake data.

### Toggle Sounds

This section explains the meaning of the various toggle sounds used in
the game.

  Sound                                          Description                                                           Played when...
  ---------------------------------------------- --------------------------------------------------------------------- -------------------------------------------------------------------------------------------
  [On](../id1/sound/toggles/on.wav)              The generic “item is activated” sound.                                Played when any device (for example the ESR, D5k or side hazard detection) is turned on.
  [Off](../id1/sound/toggles/off.wav)            The generic “item has been de-activated” sound.                       Played when any device (for example the ESR, D5k or side hazard detection) is turned off.
  [Mode switch](../id1/sound/toggles/mode.wav)   Used to indicate when a multi-mode device switches to another mode.   Played when the ESR switches from mode 1 to mode 2 or back from mode 2 to mode 1.

### Navigation Sounds

This section explains the meaning of the sounds that the navigation
helper makes.

**Table A.1. Structures**

  Sound                                                 Description                                                                             Played when...
  ----------------------------------------------------- --------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Wall](../id1/sound/nav/wall.wav)                     Sound indicating a wall has been detected.                                              Played when there is a wall near you (at a volume proportional to your distance from it). Walls are “sounded” at half the volume of stairs and doors (to stop them getting in the way).
  [Slope](../id1/sound/nav/slope.wav)                   Sound indicating a up or downwards slope (or set of stairs) has been detected.          Played when there is a slope near you (at a volume proportional to your distance from it).
  [Door](../id1/sound/nav/door.wav)                     Sound indicating a door has been detected.                                              Played when there is a door near you (at a volume proportional to your distance from it).
  Touching a Wall (in Quake's sounds)                   This indicates you're stood right next to (touching) a wall.                            Played when you're touching a wall and have wall touch warnings enabled.
  [Scraping a Wall](../id1/sound/nav/wall-scrape.wav)   This indicates you're walking but a wall is in your way and you're scraping along it.   Played when a wall is in your way but you are able to walk, sliding along it.
  [Wind](../id1/sound/nav/wind.wav)                     This indicates that a lot of empty space can be found in a certain direction.           Played when there is a large amount of empty space in a given direction from you (when a sweep has been initiated with the L key).

\
 **Table A.2. Vertical Movement**

  Sound                               Description                                            Played when...
  ----------------------------------- ------------------------------------------------------ -----------------------------------------------------
  [Up](../id1/sound/nav/up.wav)       This sound indicates you're going up in the world.     Played when you go up stairs, slopes or on lifts.
  [Down](../id1/sound/nav/down.wav)   This sound indicates you're going down in the world.   Played when you go down stairs, slopes or on lifts.

\
 **Table A.3. Hazard (Drop/Ledge) Warnings**

  Sound                                           Description               Played when...
  ----------------------------------------------- ------------------------- ----------------------------------------------------------------------------------------------------------------
  [Small drop](../id1/sound/haz/drop-small.wav)   Indicates a small drop.   Played when a small drop is detected near you (and hazard warnings and/or side hazard warnings are turned on).
  [Big drop](../id1/sound/haz/drop-big.wav)       Indicates a big drop.     Played when a big drop is detected near you (and hazard warnings and/or side hazard warnings are turned on).
  [Huge drop](../id1/sound/haz/drop-huge.wav)     Indicates a huge drop.    Played when a huge drop is detected near you (and hazard warnings and/or side hazard warnings are turned on).

\
 \#\#\#\# Jump Descriptions

When you ask if you can make a jump, you'll either be told (via speech
or Braille, depending on how you've set AudioQuake up) that you can make
it with a normal jump or you'll need to do a running jump.

If this information is not available (i.e. if there is no jump in front
of you, or you're too far away from one), you'll hear this generic
[“access denied”](../id1/sound/deny.wav)-type sound.

You'll also hear the above sound if you ask for a description of what
lies in the drop (ground, water, slime or lava) and there is no drop in
front of you or you are too far away from one.

### Independent Navigation Aid Sounds

This section explains the meaning of sounds made by the independent
navigation aids.

**Table A.4. Waypoint Marker Sounds**

  Sound                                                 Description                                 Played when...
  ----------------------------------------------------- ------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Marker homing signal](../id1/sound/nav/marker.wav)   Emanates from the marker's location.        This lets you know where a marker is. When you touch a marker, you'll be told which waypoint number it is (the number increases with every marker you add).
  [Denied](../id1/sound/deny.wav)                       Indicates that an action is not possible.   This sound is used in a number of places to let you know that you can't do something. In this case, it is played when you press the “delete last marker” key and there is no marker to delete.

\
 \#\#\#\# Compass Sounds

When you activate the compass, you will be told the name of the
direction you're pointing in (or your bearing in degrees if the
direction doesn't have a full name).

### Detector 5000 Sounds

This section explains the meaning of the sounds the D5k makes.

  Sound                                                     Description                                                                                                                                                         Played when...
  --------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------
  (standard Quake sounds)                                   The Quake “item activation” sounds (such as health, ammo, armour, weapon or power-up pickup sounds) are played to indicate what type of object has been detected.   The sounds are played when you're near an object (at a volume proportional to your distance from it).
  [Backpack](../id1/sound/d5k/backpack.wav)                 A dropped backpack. (Quake didn't have a sound for these.)                                                                                                          Played when a dropped backpack is near you. Monsters drop them when they die (if they've not been exploded).
  [Item is outside FOV](../id1/sound/d5k/outside-fov.wav)   Indicates that a D5k-detected item lies beyond your field of view.                                                                                                  Played when the D5k detects an item outside of your FOV (at a volume proportional to your distance from it).

### Weapon Sounds

When you pick up a new weapon, or switch weapons, the name of the weapon
you're using is announced.

If you run out of ammo, you'll hear the
[ammo-out](../id1/sound/ammo-out.wav) sound. You'll also hear this sound
if you try to switch to a weapon that you possess but don't have any
ammo for.

If you try to use a weapon you don't yet possess, you'll hear this
[“access denied”](../id1/sound/deny.wav) sound.

### EtherScan RADAR Sounds

This section explains the meaning of the sounds that the ESR makes.

**Table A.5. Monster Indication Sounds**

  Sound                                                            Description                                                                        Played when...
  ---------------------------------------------------------------- ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [Monster on lower level](../id1/sound/esr/monster-lower.wav)     Sound indicating that a monster is at a lower level (elevation) to the player.     Played when a monster is detected and is on the lower level as the player.
  [Monster on same level](../id1/sound/esr/monster-same.wav)       Sound indicating that a monster is at a similar level (elevation) to the player.   Played when a monster is detected and is on the same level as the player.
  [Monster on higher level](../id1/sound/esr/monster-higher.wav)   Sound indicating that a monster is at a higher level (elevation) to the player.    Played when a monster is detected and is on the higher level as the player.

\
 **Table A.6. Enemy (Player or Bot) Indication Sounds**

  Sound                                                        Description                                                                      Played when...
  ------------------------------------------------------------ -------------------------------------------------------------------------------- ---------------------------------------------------------------------------
  [Enemy on lower level](../id1/sound/esr/enemy-lower.wav)     Sound indicating that a enemy is at a lower level (elevation) to the player.     Played when a enemy is detected and is on the lower level as the player.
  [Enemy on same level](../id1/sound/esr/enemy-same.wav)       Sound indicating that a enemy is at a similar level (elevation) to the player.   Played when a enemy is detected and is on the same level as the player.
  [Enemy on higher level](../id1/sound/esr/enemy-higher.wav)   Sound indicating that a enemy is at a higher level (elevation) to the player.    Played when a enemy is detected and is on the higher level as the player.

\
 **Table A.7. Friend (Player or Bot) Indication Sounds**

  Sound                                                          Description                                                                       Played when...
  -------------------------------------------------------------- --------------------------------------------------------------------------------- ----------------------------------------------------------------------------
  [Friend on lower level](../id1/sound/esr/friend-lower.wav)     Sound indicating that a friend is at a lower level (elevation) to the player.     Played when a friend is detected and is on the lower level as the player.
  [Friend on same level](../id1/sound/esr/friend-same.wav)       Sound indicating that a friend is at a similar level (elevation) to the player.   Played when a friend is detected and is on the same level as the player.
  [Friend on higher level](../id1/sound/esr/friend-higher.wav)   Sound indicating that a friend is at a higher level (elevation) to the player.    Played when a friend is detected and is on the higher level as the player.

\
 \#\#\#\# Hazard Detection Mode

When the ESR is in mode 2 (hazard detection), it makes a [“hazard
detected” sound](../id1/sound/esr/haz.wav) if there is a near-by hazard.

### End of Level

When you complete a map, you'll hear [this delightful little
tune](../id1/sound/endlevel.wav).

Finding out More – The Web is Your Friend!
------------------------------------------

If you wish to learn anything about Quake/QuakeWorld (the online
version), the best place to look is the web. The game is still very
popular and you'll find all sorts out about console commands, server
admininstration and fancy moves when playing. A great set of starting
points is:

-   [QuakeWorld for
    Freshies](http://www.challenge-smackdown.com/qwguide/)

-   [QuakeWorld Client Console
    Commands](http://www.planetquake.com/console/commands/quakeworld_client.html)

-   [QuakeWorld Server Console
    Commands](http://www.planetquake.com/console/commands/quakeworld_server.html)

Please visit our web site and/or contact us if you need any further
information on, or help with, any aspect of AudioQuake. You can find our
contact details on the web site:

<http://www.agrip.org.uk/>

Remember that that latest version of the manual can always be found at:

<http://docs.agrip.org.uk/>

If you have any suggestions or queries relating to any aspect of the
game, the documentation or the web site, please contact us via the
addresses listed on the following page:

<http://www.agrip.org.uk/ContactUs>

Installing AudioQuake from Source
---------------------------------

This appendix is primarily aimed at developers who wish to learn how
AudioQuake works, contribute to the project or use it in their own works
(remember that if you do this, you're bound by the GNU General Public
Licence and must keep your code open).

The game can be installed from source on both Linux and Windows. The
following sections describe how this can be done.

### Installing from Source on Linux

To install from a source package on Linux, follow the procedure below:

1.  Extract the package you downloaded. For example:

    ~~~~ {.screen}
    $ tar zxf AudioQuake-0.3.0_linux-ppc.tar.gz
    ~~~~

2.  Change into this directory and run the “setup” program. This will
    guide you through most of the installation process.

    ~~~~ {.screen}
    $ cd AudioQuake-0.3.0_linux-ppc
    $ ./setup
    ~~~~

    The setup program will detect that you're using a source package and
    will inform you that you need to compile ZQuake and the QuakeC code
    in order to play the game. This can be achieved by following the
    remaining steps in this procedure.

3.  You'll need to compile “ZQCC” – ZQuake's QuakeC compiler. It can be
    found in the `zquake-cvs/zqcc/`{.filename} directory in your
    extracted source package. The program is written in C and compiling
    it is as simple as issuing the **make** command.

    Be sure to put the resultant **zqcc** binary somewhere on your path
    to make the next step more convenient.

4.  Once you've compiled **zqcc**, you can use it to compile the
    gamecode portion of AudioQuake. This is a customised version of the
    original Quake gamecode, which adds a number of accessibility
    features (such as the EtherScan RADAR and Detector 5000).

    1.  Move into the `zquake-cvs/qc/agrip/`{.filename} directory in
        your source package, then issue the following command:

        ~~~~ {.screen}
        $ zqcc -progs progs.src
        ~~~~

        This will produce the `qwprogs.dat`{.filename} file, which is
        the gamecode for the multiplayer game modes.

    2.  You'll then need to issue the same command as above but
        specifying `spprogs.dat`{.filename} instead of
        `progs.src`{.filename}, which will generate the singleplayer
        gamecode.

    3.  Finally, move the two “.dat” files to the `agrip/`{.filename}
        directory under your ZQuake installation directory (usually
        `~/.zquake/`{.filename}).

5.  Finally, you can compile the ZQuake engine itself. To do this, move
    into the `zquake-cvs/zquake/`{.filename} directory within your
    extracted source package and issue the **make** command. You'll be
    given help on what each of the make rules does. This should help you
    decide which one to use to compile the engine. For AudioQuake
    releases, we provide both the full game engine and a dedicated
    server binary.

    When compilation has finished, you can move the binary from the
    `release-architecture`{.filename}/ directory into your ZQuake
    installation directory (usually `~/.zquake/`{.filename}).

### Installing from Source on Windows

We recommend the use of [MinGW](http://www.mingw.org/),
[LCC-Win32](http://www.cs.virginia.edu/~lcc-win32/), [Open
Watcom](http://www.openwatcom.org/) or Visual C++ for compilation of
ZQuake/AudioQuake on Windows. To install from a source package on
Windows, follow the procedure below. We'll assume you're using Visual
C++ at some stages, but this shouldn't have too much of an impact on you
if you're using some of the other systems.

1.  Extract the package you downloaded. You can do this with any decent
    archiving utility (such as [7-Zip](http://www.7-zip.org/)). This
    extracted setup package will become your AudioQuake installation, so
    you might want to rename and move it so that it is convenient to get
    to.

    **Tip:** If you'd rather make your own binary setup packages from
    the source package, you can use [Inno
    Setup](http://www.jrsoftware.org/isinfo.php) on the
    `setup.iss`{.filename} file in this directory (after you've followed
    the rest of these steps. Then you can use your own customised setup
    program to install AudioQuake (which will mean that you get the
    Start Menu shortcuts, too).

2.  You'll need to compile “ZQCC” – ZQuake's QuakeC compiler. It can be
    found in the `zquake-cvs/zqcc/`{.filename} directory in your
    extracted source package. The program is written in C and can be
    compiled with your favourite C development system.

    Be sure to put the resultant **zqcc** binary somewhere on your path
    to make the next step more convenient.

3.  Once you've compiled **zqcc**, you can use it to compile the
    gamecode portion of AudioQuake. This is a customised version of the
    original Quake gamecode, which adds a number of accessibility
    features (such as the EtherScan RADAR and Detector 5000).

    1.  Move into the `zquake-cvs/qc/agrip/`{.filename} directory in
        your source package, then issue the following command:

        ~~~~ {.screen}
        > zqcc -progs progs.src
        ~~~~

        This will produce the `qwprogs.dat`{.filename} file, which is
        the gamecode for the multiplayer game modes.

    2.  You'll then need to issue the same command as above but
        specifying `spprogs.dat`{.filename} instead of
        `progs.src`{.filename}, which will generate the singleplayer
        gamecode.

    3.  Finally, move the two “.dat” files to the `agrip/`{.filename}
        directory under your extracted source package.

4.  Finally, you can compile the ZQuake engine itself. To do this, move
    into the `zquake-cvs/zquake/source/`{.filename} directory within
    your extracted source package. There are a few steps involved in
    compiling ZQuake. They're described below, with the assumption that
    you're using Visual C++.

    1.  Before you begin, you'll need to download the compile support
        tools from ZQuake's website. They're needed for compiling the
        software (non-OpenGL) version of the engine. They come in a ZIP
        file and need to be placed in the
        `zquake-cvs/zquake/source/`{.filename} directory in your
        extracted source package directory.

        The tools can be downloaded from [ZQuake download
        page](http://zquake.frag.ru/eng/download/). They're in the
        [`mgl_redist.zip`{.filename}](http://zquake.frag.ru/files/mgl_redist.zip)
        file.

    2.  Open `zquake.dsw`{.filename} with Visual C++. In the Project
        Settings dialog, make sure (on the “C/C++” tab) that you define
        a symbol called “AGRIP”. This enables the AGRIP extensions to
        the engine during compilation.

    3.  In AudioQuake releases, we provide a full game engine and a
        dedicated server binary. To compile the full game engine, make
        sure that “zquake - Win32 Release” is selected as the active
        project. You can then choose to “Build zquake.exe”

    4.  You can then set “zqds - Win32 Release” as the active project
        and choose “Build zqds.exe” from the menu.

5.  When compilation has finished, you can move the binary from the
    `release/`{.filename} directory created by your compiler into the
    extracted source package directory. If you're using this extracted
    directory as your AudioQuake installation, you can now safely
    (re)move the `zquake-cvs/`{.filename} directory from it.

Manual Revision History
-----------------------

**Revision History**

Revision 0.3.0

Day N^th^ December 2004

 

A huge number of major updates and minor tweaks to reflect the move to
ZQuake and new features introduced in the first milestone of AudioQuake.

Revision 0.2.1

Thursday 29^th^ July 2004

 

Updated for the name change and new features in 0.2.1. Updated jumping
and game save/loading instructions. Removed Perl from the installation
instructions (as it is now included in the setup package).

Revision 0.2.0

Monday 5^th^ July 2004

 

Added information on the new installer, speech integration and the
tutorial maps, plus how to move on after exiting a level. Removed
redundant information, moved the info on how to extract registered data
to the reference section. A great deal of minor updates for 0.2.0.

Revision 0.1.0

Thursday 10^th^ June 2004

 

Added section on how to obtain and set up shareware Quake. Added age
limit information. Also created the sounds reference section for beta.

Revision 0.0.2

Saturday 22^nd^ May 2004

 

Updated for the 0.0.4 release (now includes bots).

Revision 0.0.1

Tuesday 18^th^ May 2004

 

Initial version, written for AGRIP 0.0.4.

GNU General Public License
--------------------------

Version 2, June 1991

Copyright © 1989, 1991 Free Software Foundation, Inc.

Free Software Foundation, Inc. \
   51 Franklin Street, Fifth Floor, \
   Boston, \
   MA \
   02110-1301\
   USA\
 Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Version 2, June 1991

### Preamble

The licenses for most software are designed to take away your freedom to
share and change it. By contrast, the GNU General Public License is
intended to guarantee your freedom to share and change free software -
to make sure the software is free for all its users. This General Public
License applies to most of the Free Software Foundation's software and
to any other program whose authors commit to using it. (Some other Free
Software Foundation software is covered by the GNU Library General
Public License instead.) You can apply it to your programs, too.

When we speak of free software, we are referring to freedom, not price.
Our General Public Licenses are designed to make sure that you have the
freedom to distribute copies of free software (and charge for this
service if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs; and that you know you can do these things.

To protect your rights, we need to make restrictions that forbid anyone
to deny you these rights or to ask you to surrender the rights. These
restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

For example, if you distribute copies of such a program, whether gratis
or for a fee, you must give the recipients all the rights that you have.
You must make sure that they, too, receive or can get the source code.
And you must show them these terms so they know their rights.

We protect your rights with two steps:

1.  copyright the software, and

2.  offer you this license which gives you legal permission to copy,
    distribute and/or modify the software.

Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software. If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

Finally, any free program is threatened constantly by software patents.
We wish to avoid the danger that redistributors of a free program will
individually obtain patent licenses, in effect making the program
proprietary. To prevent this, we have made it clear that any patent must
be licensed for everyone's free use or not licensed at all.

The precise terms and conditions for copying, distribution and
modification follow.

### TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

#### Section 0

This License applies to any program or other work which contains a
notice placed by the copyright holder saying it may be distributed under
the terms of this General Public License. The "Program", below, refers
to any such program or work, and a “work based on the Program ” means
either the Program or any derivative work under copyright law: that is
to say, a work containing the Program or a portion of it, either
verbatim or with modifications and/or translated into another language.
(Hereinafter, translation is included without limitation in the term
“modification ”.) Each licensee is addressed as “you”.

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope. The act of running
the Program is not restricted, and the output from the Program is
covered only if its contents constitute a work based on the Program
(independent of having been made by running the Program). Whether that
is true depends on what the Program does.

#### Section 1

You may copy and distribute verbatim copies of the Program's source code
as you receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice and
disclaimer of warranty; keep intact all the notices that refer to this
License and to the absence of any warranty; and give any other
recipients of the Program a copy of this License along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

#### Section 2

You may modify your copy or copies of the Program or any portion of it,
thus forming a work based on the Program, and copy and distribute such
modifications or work under the terms of [Section
1](#gpl-2-1 "Section 1") above, provided that you also meet all of these
conditions:

1.  You must cause the modified files to carry prominent notices stating
    that you changed the files and the date of any change.

2.  You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any part
    thereof, to be licensed as a whole at no charge to all third parties
    under the terms of this License.

3.  If the modified program normally reads commands interactively when
    run, you must cause it, when started running for such interactive
    use in the most ordinary way, to print or display an announcement
    including an appropriate copyright notice and a notice that there is
    no warranty (or else, saying that you provide a warranty) and that
    users may redistribute the program under these conditions, and
    telling the user how to view a copy of this License.

    ### Exception:

    If the Program itself is interactive but does not normally print
    such an announcement, your work based on the Program is not required
    to print an announcement.)

These requirements apply to the modified work as a whole. If
identifiable sections of that work are not derived from the Program, and
can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works. But when you
distribute the same sections as part of a whole which is a work based on
the Program, the distribution of the whole must be on the terms of this
License, whose permissions for other licensees extend to the entire
whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of a
storage or distribution medium does not bring the other work under the
scope of this License.

#### Section 3

You may copy and distribute the Program (or a work based on it, under
[Section 2](#gpl-2-2 "Section 2") in object code or executable form
under the terms of [Sections 1](#gpl-2-1 "Section 1") and
[2](#gpl-2-2 "Section 2") above provided that you also do one of the
following:

1.  Accompany it with the complete corresponding machine-readable source
    code, which must be distributed under the terms of Sections 1 and 2
    above on a medium customarily used for software interchange; or,

2.  Accompany it with a written offer, valid for at least three years,
    to give any third party, for a charge no more than your cost of
    physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

3.  Accompany it with the information you received as to the offer to
    distribute corresponding source code. (This alternative is allowed
    only for noncommercial distribution and only if you received the
    program in object code or executable form with such an offer, in
    accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it. For an executable work, complete source code
means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to control
compilation and installation of the executable. However, as a special
exception, the source code distributed need not include anything that is
normally distributed (in either source or binary form) with the major
components (compiler, kernel, and so on) of the operating system on
which the executable runs, unless that component itself accompanies the
executable.

If distribution of executable or object code is made by offering access
to copy from a designated place, then offering equivalent access to copy
the source code from the same place counts as distribution of the source
code, even though third parties are not compelled to copy the source
along with the object code.

#### Section 4

You may not copy, modify, sublicense, or distribute the Program except
as expressly provided under this License. Any attempt otherwise to copy,
modify, sublicense or distribute the Program is void, and will
automatically terminate your rights under this License. However, parties
who have received copies, or rights, from you under this License will
not have their licenses terminated so long as such parties remain in
full compliance.

#### Section 5

You are not required to accept this License, since you have not signed
it. However, nothing else grants you permission to modify or distribute
the Program or its derivative works. These actions are prohibited by law
if you do not accept this License. Therefore, by modifying or
distributing the Program (or any work based on the Program), you
indicate your acceptance of this License to do so, and all its terms and
conditions for copying, distributing or modifying the Program or works
based on it.

#### Section 6

Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions. You may not impose any further restrictions
on the recipients' exercise of the rights granted herein. You are not
responsible for enforcing compliance by third parties to this License.

#### Section 7

If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License. If you cannot distribute
so as to satisfy simultaneously your obligations under this License and
any other pertinent obligations, then as a consequence you may not
distribute the Program at all. For example, if a patent license would
not permit royalty-free redistribution of the Program by all those who
receive copies directly or indirectly through you, then the only way you
could satisfy both it and this License would be to refrain entirely from
distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is implemented
by public license practices. Many people have made generous
contributions to the wide range of software distributed through that
system in reliance on consistent application of that system; it is up to
the author/donor to decide if he or she is willing to distribute
software through any other system and a licensee cannot impose that
choice.

This section is intended to make thoroughly clear what is believed to be
a consequence of the rest of this License.

#### Section 8

If the distribution and/or use of the Program is restricted in certain
countries either by patents or by copyrighted interfaces, the original
copyright holder who places the Program under this License may add an
explicit geographical distribution limitation excluding those countries,
so that distribution is permitted only in or among countries not thus
excluded. In such case, this License incorporates the limitation as if
written in the body of this License.

#### Section 9

The Free Software Foundation may publish revised and/or new versions of
the General Public License from time to time. Such new versions will be
similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number. If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and
conditions either of that version or of any later version published by
the Free Software Foundation. If the Program does not specify a version
number of this License, you may choose any version ever published by the
Free Software Foundation.

#### Section 10

If you wish to incorporate parts of the Program into other free programs
whose distribution conditions are different, write to the author to ask
for permission. For software which is copyrighted by the Free Software
Foundation, write to the Free Software Foundation; we sometimes make
exceptions for this. Our decision will be guided by the two goals of
preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

#### NO WARRANTY Section 11

BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY FOR
THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER
EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH
YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL
NECESSARY SERVICING, REPAIR OR CORRECTION.

#### Section 12

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR
DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL
DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM
(INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED
INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF
THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR
OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

END OF TERMS AND CONDITIONS

### How to Apply These Terms to Your New Programs

If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these
terms.

To do so, attach the following notices to the program. It is safest to
attach them to the start of each source file to most effectively convey
the exclusion of warranty; and each file should have at least the
"copyright" line and a pointer to where the full notice is found.

\<one line to give the program's name and a brief idea of what it
does.\> Copyright (C) \<year\> \<name of author\>

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

Gnomovision version 69, Copyright (C) year name of author Gnomovision
comes with ABSOLUTELY NO WARRANTY; for details type \`show w'. This is
free software, and you are welcome to redistribute it under certain
conditions; type \`show c' for details.

The hypothetical commands \`show w' and \`show c' should show the
appropriate parts of the General Public License. Of course, the commands
you use may be called something other than \`show w' and \`show c'; they
could even be mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary. Here is a sample; alter the names:

Yoyodyne, Inc., hereby disclaims all copyright interest in the program
\`Gnomovision' (which makes passes at compilers) written by James
Hacker.

\<signature of Ty Coon\>, 1 April 1989 Ty Coon, President of Vice

This General Public License does not permit incorporating your program
into proprietary programs. If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications
with the library. If this is what you want to do, use the GNU Library
General Public License instead of this License.

GNU Free Documentation License
------------------------------

Version 1.2, November 2002

Copyright © 2000,2001,2002 Free Software Foundation, Inc.

Free Software Foundation, Inc.\
  51 Franklin Street, Fifth Floor,\
  Boston,\
  MA\
  02110-1301\
  USA\
  

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Version 1.2, November 2002

### PREAMBLE

The purpose of this License is to make a manual, textbook, or other
functional and useful document "free" in the sense of freedom: to assure
everyone the effective freedom to copy and redistribute it, with or
without modifying it, either commercially or noncommercially.
Secondarily, this License preserves for the author and publisher a way
to get credit for their work, while not being considered responsible for
modifications made by others.

This License is a kind of "copyleft", which means that derivative works
of the document must themselves be free in the same sense. It
complements the GNU General Public License, which is a copyleft license
designed for free software.

We have designed this License in order to use it for manuals for free
software, because free software needs free documentation: a free program
should come with manuals providing the same freedoms that the software
does. But this License is not limited to software manuals; it can be
used for any textual work, regardless of subject matter or whether it is
published as a printed book. We recommend this License principally for
works whose purpose is instruction or reference.

### APPLICABILITY AND DEFINITIONS

This License applies to any manual or other work, in any medium, that
contains a notice placed by the copyright holder saying it can be
distributed under the terms of this License. Such a notice grants a
world-wide, royalty-free license, unlimited in duration, to use that
work under the conditions stated herein. The "Document", below, refers
to any such manual or work. Any member of the public is a licensee, and
is addressed as "you". You accept the license if you copy, modify or
distribute the work in a way requiring permission under copyright law.

A "Modified Version" of the Document means any work containing the
Document or a portion of it, either copied verbatim, or with
modifications and/or translated into another language.

A "Secondary Section" is a named appendix or a front-matter section of
the Document that deals exclusively with the relationship of the
publishers or authors of the Document to the Document's overall subject
(or to related matters) and contains nothing that could fall directly
within that overall subject. (Thus, if the Document is in part a
textbook of mathematics, a Secondary Section may not explain any
mathematics.) The relationship could be a matter of historical
connection with the subject or with related matters, or of legal,
commercial, philosophical, ethical or political position regarding them.

The "Invariant Sections" are certain Secondary Sections whose titles are
designated, as being those of Invariant Sections, in the notice that
says that the Document is released under this License. If a section does
not fit the above definition of Secondary then it is not allowed to be
designated as Invariant. The Document may contain zero Invariant
Sections. If the Document does not identify any Invariant Sections then
there are none.

The "Cover Texts" are certain short passages of text that are listed, as
Front-Cover Texts or Back-Cover Texts, in the notice that says that the
Document is released under this License. A Front-Cover Text may be at
most 5 words, and a Back-Cover Text may be at most 25 words.

A "Transparent" copy of the Document means a machine-readable copy,
represented in a format whose specification is available to the general
public, that is suitable for revising the document straightforwardly
with generic text editors or (for images composed of pixels) generic
paint programs or (for drawings) some widely available drawing editor,
and that is suitable for input to text formatters or for automatic
translation to a variety of formats suitable for input to text
formatters. A copy made in an otherwise Transparent file format whose
markup, or absence of markup, has been arranged to thwart or discourage
subsequent modification by readers is not Transparent. An image format
is not Transparent if used for any substantial amount of text. A copy
that is not "Transparent" is called "Opaque".

Examples of suitable formats for Transparent copies include plain ASCII
without markup, Texinfo input format, LaTeX input format, SGML or XML
using a publicly available DTD, and standard-conforming simple HTML,
PostScript or PDF designed for human modification. Examples of
transparent image formats include PNG, XCF and JPG. Opaque formats
include proprietary formats that can be read and edited only by
proprietary word processors, SGML or XML for which the DTD and/or
processing tools are not generally available, and the machine-generated
HTML, PostScript or PDF produced by some word processors for output
purposes only.

The "Title Page" means, for a printed book, the title page itself, plus
such following pages as are needed to hold, legibly, the material this
License requires to appear in the title page. For works in formats which
do not have any title page as such, "Title Page" means the text near the
most prominent appearance of the work's title, preceding the beginning
of the body of the text.

A section "Entitled XYZ" means a named subunit of the Document whose
title either is precisely XYZ or contains XYZ in parentheses following
text that translates XYZ in another language. (Here XYZ stands for a
specific section name mentioned below, such as "Acknowledgements",
"Dedications", "Endorsements", or "History".) To "Preserve the Title" of
such a section when you modify the Document means that it remains a
section "Entitled XYZ" according to this definition.

The Document may include Warranty Disclaimers next to the notice which
states that this License applies to the Document. These Warranty
Disclaimers are considered to be included by reference in this License,
but only as regards disclaiming warranties: any other implication that
these Warranty Disclaimers may have is void and has no effect on the
meaning of this License.

### VERBATIM COPYING

You may copy and distribute the Document in any medium, either
commercially or noncommercially, provided that this License, the
copyright notices, and the license notice saying this License applies to
the Document are reproduced in all copies, and that you add no other
conditions whatsoever to those of this License. You may not use
technical measures to obstruct or control the reading or further copying
of the copies you make or distribute. However, you may accept
compensation in exchange for copies. If you distribute a large enough
number of copies you must also follow the conditions in section 3.

You may also lend copies, under the same conditions stated above, and
you may publicly display copies.

### COPYING IN QUANTITY

If you publish printed copies (or copies in media that commonly have
printed covers) of the Document, numbering more than 100, and the
Document's license notice requires Cover Texts, you must enclose the
copies in covers that carry, clearly and legibly, all these Cover Texts:
Front-Cover Texts on the front cover, and Back-Cover Texts on the back
cover. Both covers must also clearly and legibly identify you as the
publisher of these copies. The front cover must present the full title
with all words of the title equally prominent and visible. You may add
other material on the covers in addition. Copying with changes limited
to the covers, as long as they preserve the title of the Document and
satisfy these conditions, can be treated as verbatim copying in other
respects.

If the required texts for either cover are too voluminous to fit
legibly, you should put the first ones listed (as many as fit
reasonably) on the actual cover, and continue the rest onto adjacent
pages.

If you publish or distribute Opaque copies of the Document numbering
more than 100, you must either include a machine-readable Transparent
copy along with each Opaque copy, or state in or with each Opaque copy a
computer-network location from which the general network-using public
has access to download using public-standard network protocols a
complete Transparent copy of the Document, free of added material. If
you use the latter option, you must take reasonably prudent steps, when
you begin distribution of Opaque copies in quantity, to ensure that this
Transparent copy will remain thus accessible at the stated location
until at least one year after the last time you distribute an Opaque
copy (directly or through your agents or retailers) of that edition to
the public.

It is requested, but not required, that you contact the authors of the
Document well before redistributing any large number of copies, to give
them a chance to provide you with an updated version of the Document.

### MODIFICATIONS

You may copy and distribute a Modified Version of the Document under the
conditions of sections 2 and 3 above, provided that you release the
Modified Version under precisely this License, with the Modified Version
filling the role of the Document, thus licensing distribution and
modification of the Modified Version to whoever possesses a copy of it.
In addition, you must do these things in the Modified Version:

**GNU FDL Modification Conditions**

1.  Use in the Title Page (and on the covers, if any) a title distinct
    from that of the Document, and from those of previous versions
    (which should, if there were any, be listed in the History section
    of the Document). You may use the same title as a previous version
    if the original publisher of that version gives permission.
2.  List on the Title Page, as authors, one or more persons or entities
    responsible for authorship of the modifications in the Modified
    Version, together with at least five of the principal authors of the
    Document (all of its principal authors, if it has fewer than five),
    unless they release you from this requirement.
3.  State on the Title page the name of the publisher of the Modified
    Version, as the publisher.
4.  Preserve all the copyright notices of the Document.
5.  Add an appropriate copyright notice for your modifications adjacent
    to the other copyright notices.
6.  Include, immediately after the copyright notices, a license notice
    giving the public permission to use the Modified Version under the
    terms of this License, in the form shown in the
    [Addendum](#gfdl-addendum "ADDENDUM: How to use this License for your documents")
    below.
7.  Preserve in that license notice the full lists of Invariant Sections
    and required Cover Texts given in the Document's license notice.
8.  Include an unaltered copy of this License.
9.  Preserve the section Entitled "History", Preserve its Title, and add
    to it an item stating at least the title, year, new authors, and
    publisher of the Modified Version as given on the Title Page. If
    there is no section Entitled "History" in the Document, create one
    stating the title, year, authors, and publisher of the Document as
    given on its Title Page, then add an item describing the Modified
    Version as stated in the previous sentence.
10. Preserve the network location, if any, given in the Document for
    public access to a Transparent copy of the Document, and likewise
    the network locations given in the Document for previous versions it
    was based on. These may be placed in the "History" section. You may
    omit a network location for a work that was published at least four
    years before the Document itself, or if the original publisher of
    the version it refers to gives permission.
11. For any section Entitled "Acknowledgements" or "Dedications",
    Preserve the Title of the section, and preserve in the section all
    the substance and tone of each of the contributor acknowledgements
    and/or dedications given therein.
12. Preserve all the Invariant Sections of the Document, unaltered in
    their text and in their titles. Section numbers or the equivalent
    are not considered part of the section titles.
13. Delete any section Entitled "Endorsements". Such a section may not
    be included in the Modified Version.
14. Do not retitle any existing section to be Entitled "Endorsements" or
    to conflict in title with any Invariant Section.
15. Preserve any Warranty Disclaimers.

If the Modified Version includes new front-matter sections or appendices
that qualify as Secondary Sections and contain no material copied from
the Document, you may at your option designate some or all of these
sections as invariant. To do this, add their titles to the list of
Invariant Sections in the Modified Version's license notice. These
titles must be distinct from any other section titles.

You may add a section Entitled "Endorsements", provided it contains
nothing but endorsements of your Modified Version by various
parties--for example, statements of peer review or that the text has
been approved by an organization as the authoritative definition of a
standard.

You may add a passage of up to five words as a Front-Cover Text, and a
passage of up to 25 words as a Back-Cover Text, to the end of the list
of Cover Texts in the Modified Version. Only one passage of Front-Cover
Text and one of Back-Cover Text may be added by (or through arrangements
made by) any one entity. If the Document already includes a cover text
for the same cover, previously added by you or by arrangement made by
the same entity you are acting on behalf of, you may not add another;
but you may replace the old one, on explicit permission from the
previous publisher that added the old one.

The author(s) and publisher(s) of the Document do not by this License
give permission to use their names for publicity for or to assert or
imply endorsement of any Modified Version.

### COMBINING DOCUMENTS

You may combine the Document with other documents released under this
License, under the terms defined in [section 4](#gfdl-4 "MODIFICATIONS")
above for modified versions, provided that you include in the
combination all of the Invariant Sections of all of the original
documents, unmodified, and list them all as Invariant Sections of your
combined work in its license notice, and that you preserve all their
Warranty Disclaimers.

The combined work need only contain one copy of this License, and
multiple identical Invariant Sections may be replaced with a single
copy. If there are multiple Invariant Sections with the same name but
different contents, make the title of each such section unique by adding
at the end of it, in parentheses, the name of the original author or
publisher of that section if known, or else a unique number. Make the
same adjustment to the section titles in the list of Invariant Sections
in the license notice of the combined work.

In the combination, you must combine any sections Entitled "History" in
the various original documents, forming one section Entitled "History";
likewise combine any sections Entitled "Acknowledgements", and any
sections Entitled "Dedications". You must delete all sections Entitled
"Endorsements".

### COLLECTIONS OF DOCUMENTS

You may make a collection consisting of the Document and other documents
released under this License, and replace the individual copies of this
License in the various documents with a single copy that is included in
the collection, provided that you follow the rules of this License for
verbatim copying of each of the documents in all other respects.

You may extract a single document from such a collection, and distribute
it individually under this License, provided you insert a copy of this
License into the extracted document, and follow this License in all
other respects regarding verbatim copying of that document.

### AGGREGATION WITH INDEPENDENT WORKS

A compilation of the Document or its derivatives with other separate and
independent documents or works, in or on a volume of a storage or
distribution medium, is called an "aggregate" if the copyright resulting
from the compilation is not used to limit the legal rights of the
compilation's users beyond what the individual works permit. When the
Document is included in an aggregate, this License does not apply to the
other works in the aggregate which are not themselves derivative works
of the Document.

If the Cover Text requirement of section 3 is applicable to these copies
of the Document, then if the Document is less than one half of the
entire aggregate, the Document's Cover Texts may be placed on covers
that bracket the Document within the aggregate, or the electronic
equivalent of covers if the Document is in electronic form. Otherwise
they must appear on printed covers that bracket the whole aggregate.

### TRANSLATION

Translation is considered a kind of modification, so you may distribute
translations of the Document under the terms of section 4. Replacing
Invariant Sections with translations requires special permission from
their copyright holders, but you may include translations of some or all
Invariant Sections in addition to the original versions of these
Invariant Sections. You may include a translation of this License, and
all the license notices in the Document, and any Warranty Disclaimers,
provided that you also include the original English version of this
License and the original versions of those notices and disclaimers. In
case of a disagreement between the translation and the original version
of this License or a notice or disclaimer, the original version will
prevail.

If a section in the Document is Entitled "Acknowledgements",
"Dedications", or "History", the requirement (section 4) to Preserve its
Title (section 1) will typically require changing the actual title.

### TERMINATION

You may not copy, modify, sublicense, or distribute the Document except
as expressly provided for under this License. Any other attempt to copy,
modify, sublicense or distribute the Document is void, and will
automatically terminate your rights under this License. However, parties
who have received copies, or rights, from you under this License will
not have their licenses terminated so long as such parties remain in
full compliance.

### FUTURE REVISIONS OF THIS LICENSE

The Free Software Foundation may publish new, revised versions of the
GNU Free Documentation License from time to time. Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns. See http://www.gnu.org/copyleft/.

Each version of the License is given a distinguishing version number. If
the Document specifies that a particular numbered version of this
License "or any later version" applies to it, you have the option of
following the terms and conditions either of that specified version or
of any later version that has been published (not as a draft) by the
Free Software Foundation. If the Document does not specify a version
number of this License, you may choose any version ever published (not
as a draft) by the Free Software Foundation.

### ADDENDUM: How to use this License for your documents

To use this License in a document you have written, include a copy of
the License in the document and put the following copyright and license
notices just after the title page:

> **Sample Invariant Sections list**
>
> Copyright (c) YEAR YOUR NAME. Permission is granted to copy,
> distribute and/or modify this document under the terms of the GNU Free
> Documentation License, Version 1.2 or any later version published by
> the Free Software Foundation; with no Invariant Sections, no
> Front-Cover Texts, and no Back-Cover Texts. A copy of the license is
> included in the section entitled "GNU Free Documentation License".

If you have Invariant Sections, Front-Cover Texts and Back-Cover Texts,
replace the "with...Texts." line with this:

> **Sample Invariant Sections list**
>
> with the Invariant Sections being LIST THEIR TITLES, with the
> Front-Cover Texts being LIST, and with the Back-Cover Texts being
> LIST.

If you have Invariant Sections without Cover Texts, or some other
combination of the three, merge those two alternatives to suit the
situation.

If your document contains nontrivial examples of program code, we
recommend releasing these examples in parallel under your choice of free
software license, such as the GNU General Public License, to permit
their use in free software.