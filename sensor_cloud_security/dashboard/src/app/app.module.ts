import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule, Http } from '@angular/http';
import { MaterialModule } from '@angular/material';
import 'hammerjs';

import { LoginService } from './services/login.service';
import { UserService } from './services/user.service';
import { MonitorService } from './services/monitor.service';

import { AppComponent } from './app.component';

import { CoreModule } from './core/core.module';
import { LayoutModule } from './layout/layout.module';
import { SharedModule } from './shared/shared.module';
import { RoutesModule } from './routes/routes.module';
import { MyAccountComponent } from './my-account/my-account.component';
import { MonitorComponent } from './routes/forms/monitor/monitor.component';

import {TranslateStaticLoader, TranslateModule, TranslateLoader} from "ng2-translate";

// https://github.com/ocombe/ng2-translate/issues/218
export function createTranslateLoader(http: Http) {
    return new TranslateStaticLoader(http, './assets/i18n', '.json');
}

@NgModule({
    declarations: [
        AppComponent,
        MyAccountComponent,
    ],
    imports: [
        BrowserModule,
        CoreModule,
        LayoutModule,
        HttpModule,
        MaterialModule,
        SharedModule.forRoot(),
        RoutesModule,
        TranslateModule.forRoot({
            provide: TranslateLoader,
            useFactory: (createTranslateLoader),
            deps: [Http]
        })
    ],
    providers: [
        LoginService,
        UserService,
        MonitorService,
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }
