import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TablerefreshComponent } from './tablerefresh.component';

describe('TablerefreshComponent', () => {
  let component: TablerefreshComponent;
  let fixture: ComponentFixture<TablerefreshComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TablerefreshComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TablerefreshComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
