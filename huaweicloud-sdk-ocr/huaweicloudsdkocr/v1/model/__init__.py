# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkocr.v1.model.acceptance_bill_request_body import AcceptanceBillRequestBody
from huaweicloudsdkocr.v1.model.acceptance_bill_result import AcceptanceBillResult
from huaweicloudsdkocr.v1.model.auto_classification_request_body import AutoClassificationRequestBody
from huaweicloudsdkocr.v1.model.auto_classification_result import AutoClassificationResult
from huaweicloudsdkocr.v1.model.auto_classification_result_status import AutoClassificationResultStatus
from huaweicloudsdkocr.v1.model.auto_id_doc_classification_alarm_confidence import AutoIdDocClassificationAlarmConfidence
from huaweicloudsdkocr.v1.model.auto_id_doc_classification_alarm_result import AutoIdDocClassificationAlarmResult
from huaweicloudsdkocr.v1.model.auto_id_doc_classification_request_body import AutoIdDocClassificationRequestBody
from huaweicloudsdkocr.v1.model.auto_id_doc_classification_result import AutoIdDocClassificationResult
from huaweicloudsdkocr.v1.model.bank_receipt_dict import BankReceiptDict
from huaweicloudsdkocr.v1.model.bank_receipt_kv_pair import BankReceiptKvPair
from huaweicloudsdkocr.v1.model.bank_receipt_request_body import BankReceiptRequestBody
from huaweicloudsdkocr.v1.model.bank_receipt_result import BankReceiptResult
from huaweicloudsdkocr.v1.model.bankcard_request_body import BankcardRequestBody
from huaweicloudsdkocr.v1.model.bankcard_result import BankcardResult
from huaweicloudsdkocr.v1.model.belong_item_list import BelongItemList
from huaweicloudsdkocr.v1.model.beneficiary_item import BeneficiaryItem
from huaweicloudsdkocr.v1.model.business_card_request_body import BusinessCardRequestBody
from huaweicloudsdkocr.v1.model.business_card_result import BusinessCardResult
from huaweicloudsdkocr.v1.model.business_license_request_body import BusinessLicenseRequestBody
from huaweicloudsdkocr.v1.model.business_license_result import BusinessLicenseResult
from huaweicloudsdkocr.v1.model.cambodian_id_card_request_body import CambodianIdCardRequestBody
from huaweicloudsdkocr.v1.model.cambodian_id_card_result import CambodianIdCardResult
from huaweicloudsdkocr.v1.model.cambodian_id_card_score_information_result import CambodianIdCardScoreInformationResult
from huaweicloudsdkocr.v1.model.char_list_iem import CharListIem
from huaweicloudsdkocr.v1.model.chile_id_card_confidence import ChileIdCardConfidence
from huaweicloudsdkocr.v1.model.chile_id_card_request_body import ChileIdCardRequestBody
from huaweicloudsdkocr.v1.model.chile_id_card_result import ChileIdCardResult
from huaweicloudsdkocr.v1.model.colombia_id_card_request_body import ColombiaIdCardRequestBody
from huaweicloudsdkocr.v1.model.colombia_id_card_result import ColombiaIdCardResult
from huaweicloudsdkocr.v1.model.custom_template_request_body import CustomTemplateRequestBody
from huaweicloudsdkocr.v1.model.driver_license_back import DriverLicenseBack
from huaweicloudsdkocr.v1.model.driver_license_front import DriverLicenseFront
from huaweicloudsdkocr.v1.model.driver_license_request_body import DriverLicenseRequestBody
from huaweicloudsdkocr.v1.model.driver_license_result import DriverLicenseResult
from huaweicloudsdkocr.v1.model.exit_entry_permit_confidence import ExitEntryPermitConfidence
from huaweicloudsdkocr.v1.model.exit_entry_permit_endorsement_info import ExitEntryPermitEndorsementInfo
from huaweicloudsdkocr.v1.model.exit_entry_permit_request_body import ExitEntryPermitRequestBody
from huaweicloudsdkocr.v1.model.exit_entry_permit_result import ExitEntryPermitResult
from huaweicloudsdkocr.v1.model.extra_info_list import ExtraInfoList
from huaweicloudsdkocr.v1.model.financial_statement_request_body import FinancialStatementRequestBody
from huaweicloudsdkocr.v1.model.financial_statement_result import FinancialStatementResult
from huaweicloudsdkocr.v1.model.financial_statement_result_image_size import FinancialStatementResultImageSize
from huaweicloudsdkocr.v1.model.financial_statement_words_block_list import FinancialStatementWordsBlockList
from huaweicloudsdkocr.v1.model.financial_statement_words_region_list import FinancialStatementWordsRegionList
from huaweicloudsdkocr.v1.model.flight_itinerary_request_body import FlightItineraryRequestBody
from huaweicloudsdkocr.v1.model.flight_itinerary_result import FlightItineraryResult
from huaweicloudsdkocr.v1.model.general_table_request_body import GeneralTableRequestBody
from huaweicloudsdkocr.v1.model.general_table_result import GeneralTableResult
from huaweicloudsdkocr.v1.model.general_table_words_block_list import GeneralTableWordsBlockList
from huaweicloudsdkocr.v1.model.general_text_char_list import GeneralTextCharList
from huaweicloudsdkocr.v1.model.general_text_request_body import GeneralTextRequestBody
from huaweicloudsdkocr.v1.model.general_text_result import GeneralTextResult
from huaweicloudsdkocr.v1.model.general_text_words_block_list import GeneralTextWordsBlockList
from huaweicloudsdkocr.v1.model.handwriting_request_body import HandwritingRequestBody
from huaweicloudsdkocr.v1.model.handwriting_result import HandwritingResult
from huaweicloudsdkocr.v1.model.handwriting_words_block_list import HandwritingWordsBlockList
from huaweicloudsdkocr.v1.model.health_code_request_body import HealthCodeRequestBody
from huaweicloudsdkocr.v1.model.health_code_result import HealthCodeResult
from huaweicloudsdkocr.v1.model.health_code_words_block_list import HealthCodeWordsBlockList
from huaweicloudsdkocr.v1.model.hk_id_card_request_body import HkIdCardRequestBody
from huaweicloudsdkocr.v1.model.hk_id_card_result import HkIdCardResult
from huaweicloudsdkocr.v1.model.household_register_content import HouseholdRegisterContent
from huaweicloudsdkocr.v1.model.household_register_request_body import HouseholdRegisterRequestBody
from huaweicloudsdkocr.v1.model.household_register_result import HouseholdRegisterResult
from huaweicloudsdkocr.v1.model.id_card_request_body import IdCardRequestBody
from huaweicloudsdkocr.v1.model.id_card_result import IdCardResult
from huaweicloudsdkocr.v1.model.id_document_item import IdDocumentItem
from huaweicloudsdkocr.v1.model.id_document_request_body import IdDocumentRequestBody
from huaweicloudsdkocr.v1.model.idcard_back_result import IdcardBackResult
from huaweicloudsdkocr.v1.model.idcard_back_verification_result import IdcardBackVerificationResult
from huaweicloudsdkocr.v1.model.idcard_front_result import IdcardFrontResult
from huaweicloudsdkocr.v1.model.idcard_front_verification_result import IdcardFrontVerificationResult
from huaweicloudsdkocr.v1.model.idcard_score_info_result import IdcardScoreInfoResult
from huaweicloudsdkocr.v1.model.idcard_verification_result import IdcardVerificationResult
from huaweicloudsdkocr.v1.model.insurance_item import InsuranceItem
from huaweicloudsdkocr.v1.model.insurance_policy_detail import InsurancePolicyDetail
from huaweicloudsdkocr.v1.model.insurance_policy_request_body import InsurancePolicyRequestBody
from huaweicloudsdkocr.v1.model.insurance_policy_result import InsurancePolicyResult
from huaweicloudsdkocr.v1.model.insurant_item import InsurantItem
from huaweicloudsdkocr.v1.model.invoice_verification_request_body import InvoiceVerificationRequestBody
from huaweicloudsdkocr.v1.model.item_list import ItemList
from huaweicloudsdkocr.v1.model.itinerary_list import ItineraryList
from huaweicloudsdkocr.v1.model.license_plate_request_body import LicensePlateRequestBody
from huaweicloudsdkocr.v1.model.license_plate_result import LicensePlateResult
from huaweicloudsdkocr.v1.model.macao_id_card_request_body import MacaoIdCardRequestBody
from huaweicloudsdkocr.v1.model.macao_id_card_result import MacaoIdCardResult
from huaweicloudsdkocr.v1.model.mainland_travel_permit_confidence import MainlandTravelPermitConfidence
from huaweicloudsdkocr.v1.model.mainland_travel_permit_request_body import MainlandTravelPermitRequestBody
from huaweicloudsdkocr.v1.model.mainland_travel_permit_result import MainlandTravelPermitResult
from huaweicloudsdkocr.v1.model.mvs_invoice_request_body import MvsInvoiceRequestBody
from huaweicloudsdkocr.v1.model.mvs_invoice_result import MvsInvoiceResult
from huaweicloudsdkocr.v1.model.myanmar_driver_license_confidence import MyanmarDriverLicenseConfidence
from huaweicloudsdkocr.v1.model.myanmar_driver_license_request_body import MyanmarDriverLicenseRequestBody
from huaweicloudsdkocr.v1.model.myanmar_driver_license_result import MyanmarDriverLicenseResult
from huaweicloudsdkocr.v1.model.myanmar_idcard_confidence import MyanmarIdcardConfidence
from huaweicloudsdkocr.v1.model.myanmar_idcard_request_body import MyanmarIdcardRequestBody
from huaweicloudsdkocr.v1.model.myanmar_idcard_result import MyanmarIdcardResult
from huaweicloudsdkocr.v1.model.myanmar_idcard_translation_info import MyanmarIdcardTranslationInfo
from huaweicloudsdkocr.v1.model.passenger_travel_item_list import PassengerTravelItemList
from huaweicloudsdkocr.v1.model.passport_request_body import PassportRequestBody
from huaweicloudsdkocr.v1.model.passport_result import PassportResult
from huaweicloudsdkocr.v1.model.pcr_test_record_confidence import PcrTestRecordConfidence
from huaweicloudsdkocr.v1.model.pcr_test_record_request_body import PcrTestRecordRequestBody
from huaweicloudsdkocr.v1.model.pcr_test_record_result import PcrTestRecordResult
from huaweicloudsdkocr.v1.model.pcr_test_record_words_block_list import PcrTestRecordWordsBlockList
from huaweicloudsdkocr.v1.model.peru_id_card_request_body import PeruIdCardRequestBody
from huaweicloudsdkocr.v1.model.peru_id_card_result import PeruIdCardResult
from huaweicloudsdkocr.v1.model.qualification_category import QualificationCategory
from huaweicloudsdkocr.v1.model.qualification_category_confidence import QualificationCategoryConfidence
from huaweicloudsdkocr.v1.model.qualification_certificate_request_body import QualificationCertificateRequestBody
from huaweicloudsdkocr.v1.model.qualification_certificate_result import QualificationCertificateResult
from huaweicloudsdkocr.v1.model.qualification_confidence import QualificationConfidence
from huaweicloudsdkocr.v1.model.quota_invoice_request_body import QuotaInvoiceRequestBody
from huaweicloudsdkocr.v1.model.quota_invoice_result import QuotaInvoiceResult
from huaweicloudsdkocr.v1.model.real_estate_certificate_request_body import RealEstateCertificateRequestBody
from huaweicloudsdkocr.v1.model.real_estate_certificate_result import RealEstateCertificateResult
from huaweicloudsdkocr.v1.model.recognize_acceptance_bill_request import RecognizeAcceptanceBillRequest
from huaweicloudsdkocr.v1.model.recognize_acceptance_bill_response import RecognizeAcceptanceBillResponse
from huaweicloudsdkocr.v1.model.recognize_auto_classification_request import RecognizeAutoClassificationRequest
from huaweicloudsdkocr.v1.model.recognize_auto_classification_response import RecognizeAutoClassificationResponse
from huaweicloudsdkocr.v1.model.recognize_auto_id_doc_classification_request import RecognizeAutoIdDocClassificationRequest
from huaweicloudsdkocr.v1.model.recognize_auto_id_doc_classification_response import RecognizeAutoIdDocClassificationResponse
from huaweicloudsdkocr.v1.model.recognize_bank_receipt_request import RecognizeBankReceiptRequest
from huaweicloudsdkocr.v1.model.recognize_bank_receipt_response import RecognizeBankReceiptResponse
from huaweicloudsdkocr.v1.model.recognize_bankcard_request import RecognizeBankcardRequest
from huaweicloudsdkocr.v1.model.recognize_bankcard_response import RecognizeBankcardResponse
from huaweicloudsdkocr.v1.model.recognize_business_card_request import RecognizeBusinessCardRequest
from huaweicloudsdkocr.v1.model.recognize_business_card_response import RecognizeBusinessCardResponse
from huaweicloudsdkocr.v1.model.recognize_business_license_request import RecognizeBusinessLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_business_license_response import RecognizeBusinessLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_cambodian_id_card_request import RecognizeCambodianIdCardRequest
from huaweicloudsdkocr.v1.model.recognize_cambodian_id_card_response import RecognizeCambodianIdCardResponse
from huaweicloudsdkocr.v1.model.recognize_chile_id_card_request import RecognizeChileIdCardRequest
from huaweicloudsdkocr.v1.model.recognize_chile_id_card_response import RecognizeChileIdCardResponse
from huaweicloudsdkocr.v1.model.recognize_colombia_id_card_request import RecognizeColombiaIdCardRequest
from huaweicloudsdkocr.v1.model.recognize_colombia_id_card_response import RecognizeColombiaIdCardResponse
from huaweicloudsdkocr.v1.model.recognize_custom_template_request import RecognizeCustomTemplateRequest
from huaweicloudsdkocr.v1.model.recognize_custom_template_response import RecognizeCustomTemplateResponse
from huaweicloudsdkocr.v1.model.recognize_driver_license_request import RecognizeDriverLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_driver_license_response import RecognizeDriverLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_exit_entry_permit_request import RecognizeExitEntryPermitRequest
from huaweicloudsdkocr.v1.model.recognize_exit_entry_permit_response import RecognizeExitEntryPermitResponse
from huaweicloudsdkocr.v1.model.recognize_financial_statement_request import RecognizeFinancialStatementRequest
from huaweicloudsdkocr.v1.model.recognize_financial_statement_response import RecognizeFinancialStatementResponse
from huaweicloudsdkocr.v1.model.recognize_flight_itinerary_request import RecognizeFlightItineraryRequest
from huaweicloudsdkocr.v1.model.recognize_flight_itinerary_response import RecognizeFlightItineraryResponse
from huaweicloudsdkocr.v1.model.recognize_general_table_request import RecognizeGeneralTableRequest
from huaweicloudsdkocr.v1.model.recognize_general_table_response import RecognizeGeneralTableResponse
from huaweicloudsdkocr.v1.model.recognize_general_text_request import RecognizeGeneralTextRequest
from huaweicloudsdkocr.v1.model.recognize_general_text_response import RecognizeGeneralTextResponse
from huaweicloudsdkocr.v1.model.recognize_handwriting_request import RecognizeHandwritingRequest
from huaweicloudsdkocr.v1.model.recognize_handwriting_response import RecognizeHandwritingResponse
from huaweicloudsdkocr.v1.model.recognize_health_code_request import RecognizeHealthCodeRequest
from huaweicloudsdkocr.v1.model.recognize_health_code_response import RecognizeHealthCodeResponse
from huaweicloudsdkocr.v1.model.recognize_hk_id_card_request import RecognizeHkIdCardRequest
from huaweicloudsdkocr.v1.model.recognize_hk_id_card_response import RecognizeHkIdCardResponse
from huaweicloudsdkocr.v1.model.recognize_household_register_request import RecognizeHouseholdRegisterRequest
from huaweicloudsdkocr.v1.model.recognize_household_register_response import RecognizeHouseholdRegisterResponse
from huaweicloudsdkocr.v1.model.recognize_id_card_request import RecognizeIdCardRequest
from huaweicloudsdkocr.v1.model.recognize_id_card_response import RecognizeIdCardResponse
from huaweicloudsdkocr.v1.model.recognize_id_document_request import RecognizeIdDocumentRequest
from huaweicloudsdkocr.v1.model.recognize_id_document_response import RecognizeIdDocumentResponse
from huaweicloudsdkocr.v1.model.recognize_insurance_policy_request import RecognizeInsurancePolicyRequest
from huaweicloudsdkocr.v1.model.recognize_insurance_policy_response import RecognizeInsurancePolicyResponse
from huaweicloudsdkocr.v1.model.recognize_invoice_verification_request import RecognizeInvoiceVerificationRequest
from huaweicloudsdkocr.v1.model.recognize_invoice_verification_response import RecognizeInvoiceVerificationResponse
from huaweicloudsdkocr.v1.model.recognize_license_plate_request import RecognizeLicensePlateRequest
from huaweicloudsdkocr.v1.model.recognize_license_plate_response import RecognizeLicensePlateResponse
from huaweicloudsdkocr.v1.model.recognize_macao_id_card_request import RecognizeMacaoIdCardRequest
from huaweicloudsdkocr.v1.model.recognize_macao_id_card_response import RecognizeMacaoIdCardResponse
from huaweicloudsdkocr.v1.model.recognize_mainland_travel_permit_request import RecognizeMainlandTravelPermitRequest
from huaweicloudsdkocr.v1.model.recognize_mainland_travel_permit_response import RecognizeMainlandTravelPermitResponse
from huaweicloudsdkocr.v1.model.recognize_mvs_invoice_request import RecognizeMvsInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_mvs_invoice_response import RecognizeMvsInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_myanmar_driver_license_request import RecognizeMyanmarDriverLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_myanmar_driver_license_response import RecognizeMyanmarDriverLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_myanmar_idcard_request import RecognizeMyanmarIdcardRequest
from huaweicloudsdkocr.v1.model.recognize_myanmar_idcard_response import RecognizeMyanmarIdcardResponse
from huaweicloudsdkocr.v1.model.recognize_passport_request import RecognizePassportRequest
from huaweicloudsdkocr.v1.model.recognize_passport_response import RecognizePassportResponse
from huaweicloudsdkocr.v1.model.recognize_pcr_test_record_request import RecognizePcrTestRecordRequest
from huaweicloudsdkocr.v1.model.recognize_pcr_test_record_response import RecognizePcrTestRecordResponse
from huaweicloudsdkocr.v1.model.recognize_peru_id_card_request import RecognizePeruIdCardRequest
from huaweicloudsdkocr.v1.model.recognize_peru_id_card_response import RecognizePeruIdCardResponse
from huaweicloudsdkocr.v1.model.recognize_qualification_certificate_request import RecognizeQualificationCertificateRequest
from huaweicloudsdkocr.v1.model.recognize_qualification_certificate_response import RecognizeQualificationCertificateResponse
from huaweicloudsdkocr.v1.model.recognize_quota_invoice_request import RecognizeQuotaInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_quota_invoice_response import RecognizeQuotaInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_real_estate_certificate_request import RecognizeRealEstateCertificateRequest
from huaweicloudsdkocr.v1.model.recognize_real_estate_certificate_response import RecognizeRealEstateCertificateResponse
from huaweicloudsdkocr.v1.model.recognize_seal_request import RecognizeSealRequest
from huaweicloudsdkocr.v1.model.recognize_seal_response import RecognizeSealResponse
from huaweicloudsdkocr.v1.model.recognize_smart_document_recognizer_request import RecognizeSmartDocumentRecognizerRequest
from huaweicloudsdkocr.v1.model.recognize_smart_document_recognizer_response import RecognizeSmartDocumentRecognizerResponse
from huaweicloudsdkocr.v1.model.recognize_taxi_invoice_request import RecognizeTaxiInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_taxi_invoice_response import RecognizeTaxiInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_thailand_idcard_request import RecognizeThailandIdcardRequest
from huaweicloudsdkocr.v1.model.recognize_thailand_idcard_response import RecognizeThailandIdcardResponse
from huaweicloudsdkocr.v1.model.recognize_thailand_license_plate_request import RecognizeThailandLicensePlateRequest
from huaweicloudsdkocr.v1.model.recognize_thailand_license_plate_response import RecognizeThailandLicensePlateResponse
from huaweicloudsdkocr.v1.model.recognize_toll_invoice_request import RecognizeTollInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_toll_invoice_response import RecognizeTollInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_train_ticket_request import RecognizeTrainTicketRequest
from huaweicloudsdkocr.v1.model.recognize_train_ticket_response import RecognizeTrainTicketResponse
from huaweicloudsdkocr.v1.model.recognize_transportation_license_request import RecognizeTransportationLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_transportation_license_response import RecognizeTransportationLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_request import RecognizeVatInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_response import RecognizeVatInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_vehicle_certificate_request import RecognizeVehicleCertificateRequest
from huaweicloudsdkocr.v1.model.recognize_vehicle_certificate_response import RecognizeVehicleCertificateResponse
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_request import RecognizeVehicleLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_response import RecognizeVehicleLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_vietnam_id_card_request import RecognizeVietnamIdCardRequest
from huaweicloudsdkocr.v1.model.recognize_vietnam_id_card_response import RecognizeVietnamIdCardResponse
from huaweicloudsdkocr.v1.model.recognize_vin_request import RecognizeVinRequest
from huaweicloudsdkocr.v1.model.recognize_vin_response import RecognizeVinResponse
from huaweicloudsdkocr.v1.model.recognize_waybill_electronic_request import RecognizeWaybillElectronicRequest
from huaweicloudsdkocr.v1.model.recognize_waybill_electronic_response import RecognizeWaybillElectronicResponse
from huaweicloudsdkocr.v1.model.recognize_web_image_request import RecognizeWebImageRequest
from huaweicloudsdkocr.v1.model.recognize_web_image_response import RecognizeWebImageResponse
from huaweicloudsdkocr.v1.model.seal_list import SealList
from huaweicloudsdkocr.v1.model.seal_request_body import SealRequestBody
from huaweicloudsdkocr.v1.model.seal_result import SealResult
from huaweicloudsdkocr.v1.model.seal_words_block_list import SealWordsBlockList
from huaweicloudsdkocr.v1.model.smart_document_recognizer_form_result import SmartDocumentRecognizerFormResult
from huaweicloudsdkocr.v1.model.smart_document_recognizer_formula_block import SmartDocumentRecognizerFormulaBlock
from huaweicloudsdkocr.v1.model.smart_document_recognizer_formula_result import SmartDocumentRecognizerFormulaResult
from huaweicloudsdkocr.v1.model.smart_document_recognizer_kv_block import SmartDocumentRecognizerKVBlock
from huaweicloudsdkocr.v1.model.smart_document_recognizer_kv_words_block import SmartDocumentRecognizerKVWordsBlock
from huaweicloudsdkocr.v1.model.smart_document_recognizer_kv_result import SmartDocumentRecognizerKvResult
from huaweicloudsdkocr.v1.model.smart_document_recognizer_layout_block import SmartDocumentRecognizerLayoutBlock
from huaweicloudsdkocr.v1.model.smart_document_recognizer_layout_result import SmartDocumentRecognizerLayoutResult
from huaweicloudsdkocr.v1.model.smart_document_recognizer_ocr_result import SmartDocumentRecognizerOcrResult
from huaweicloudsdkocr.v1.model.smart_document_recognizer_request_body import SmartDocumentRecognizerRequestBody
from huaweicloudsdkocr.v1.model.smart_document_recognizer_result import SmartDocumentRecognizerResult
from huaweicloudsdkocr.v1.model.smart_document_recognizer_table_block import SmartDocumentRecognizerTableBlock
from huaweicloudsdkocr.v1.model.smart_document_recognizer_table_result import SmartDocumentRecognizerTableResult
from huaweicloudsdkocr.v1.model.smart_document_recognizer_table_words_block import SmartDocumentRecognizerTableWordsBlock
from huaweicloudsdkocr.v1.model.smart_document_recognizer_words_block_list import SmartDocumentRecognizerWordsBlockList
from huaweicloudsdkocr.v1.model.taxi_invoice_request_body import TaxiInvoiceRequestBody
from huaweicloudsdkocr.v1.model.taxi_invoice_result import TaxiInvoiceResult
from huaweicloudsdkocr.v1.model.thailand_idcard_confidence import ThailandIdcardConfidence
from huaweicloudsdkocr.v1.model.thailand_idcard_request_body import ThailandIdcardRequestBody
from huaweicloudsdkocr.v1.model.thailand_idcard_result import ThailandIdcardResult
from huaweicloudsdkocr.v1.model.thailand_license_plate_item import ThailandLicensePlateItem
from huaweicloudsdkocr.v1.model.thailand_license_plate_request_body import ThailandLicensePlateRequestBody
from huaweicloudsdkocr.v1.model.toll_invoice_request_body import TollInvoiceRequestBody
from huaweicloudsdkocr.v1.model.toll_invoice_result import TollInvoiceResult
from huaweicloudsdkocr.v1.model.train_ticket_request_body import TrainTicketRequestBody
from huaweicloudsdkocr.v1.model.train_ticket_result import TrainTicketResult
from huaweicloudsdkocr.v1.model.transportation_license_request_body import TransportationLicenseRequestBody
from huaweicloudsdkocr.v1.model.transportation_license_result import TransportationLicenseResult
from huaweicloudsdkocr.v1.model.vin_result import VINResult
from huaweicloudsdkocr.v1.model.vat_invoice_request_body import VatInvoiceRequestBody
from huaweicloudsdkocr.v1.model.vat_invoice_result import VatInvoiceResult
from huaweicloudsdkocr.v1.model.vehicle_certificate_request_body import VehicleCertificateRequestBody
from huaweicloudsdkocr.v1.model.vehicle_certificate_result import VehicleCertificateResult
from huaweicloudsdkocr.v1.model.vehicle_license_front import VehicleLicenseFront
from huaweicloudsdkocr.v1.model.vehicle_license_request_body import VehicleLicenseRequestBody
from huaweicloudsdkocr.v1.model.vehicle_license_result import VehicleLicenseResult
from huaweicloudsdkocr.v1.model.vehicle_licenseback import VehicleLicenseback
from huaweicloudsdkocr.v1.model.vietnam_id_card_request_body import VietnamIdCardRequestBody
from huaweicloudsdkocr.v1.model.vietnam_id_card_result import VietnamIdCardResult
from huaweicloudsdkocr.v1.model.vin_request_body import VinRequestBody
from huaweicloudsdkocr.v1.model.waybill_electronic_request_body import WaybillElectronicRequestBody
from huaweicloudsdkocr.v1.model.waybill_electronic_result import WaybillElectronicResult
from huaweicloudsdkocr.v1.model.web_image_contact_info import WebImageContactInfo
from huaweicloudsdkocr.v1.model.web_image_extracted_data import WebImageExtractedData
from huaweicloudsdkocr.v1.model.web_image_image_size import WebImageImageSize
from huaweicloudsdkocr.v1.model.web_image_request_body import WebImageRequestBody
from huaweicloudsdkocr.v1.model.web_image_result import WebImageResult
from huaweicloudsdkocr.v1.model.web_image_words_block_list import WebImageWordsBlockList
from huaweicloudsdkocr.v1.model.words_list_iem import WordsListIem
from huaweicloudsdkocr.v1.model.words_region_list import WordsRegionList
