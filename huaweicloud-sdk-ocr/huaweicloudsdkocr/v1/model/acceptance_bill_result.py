# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AcceptanceBillResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issue_date': 'str',
        'due_date': 'str',
        'bill_status': 'str',
        'bill_number': 'str',
        'issuer_full_name': 'str',
        'issuer_account': 'str',
        'issuer_bank_name': 'str',
        'issuer_bank_number': 'str',
        'payee_full_name': 'str',
        'payee_account': 'str',
        'payee_bank_name': 'str',
        'payee_bank_number': 'str',
        'issuance_guarantor_name': 'str',
        'issuance_guarantor_address': 'str',
        'issuance_guarantor_account': 'str',
        'issuance_guarantee_date': 'str',
        'issuance_guarantor_bank_number': 'str',
        'issuance_guarantor_bank_name': 'str',
        'amount_in_words': 'str',
        'amount_in_figures': 'str',
        'acceptor_full_name': 'str',
        'acceptor_account': 'str',
        'acceptor_bank_number': 'str',
        'acceptor_bank_name': 'str',
        'contract_number': 'str',
        'assignability': 'str',
        'issuer_commitment': 'str',
        'acceptor_commitment': 'str',
        'acceptance_date': 'str',
        'acceptance_guarantor_name': 'str',
        'acceptance_guarantor_address': 'str',
        'acceptance_guarantor_account': 'str',
        'acceptance_guarantee_date': 'str',
        'acceptance_guarantor_bank_number': 'str',
        'acceptance_guarantor_bank_name': 'str',
        'issuer_rating_entity': 'str',
        'issuer_credit_rating': 'str',
        'issuer_rating_due_date': 'str',
        'acceptor_rating_entity': 'str',
        'acceptor_credit_rating': 'str',
        'acceptor_rating_due_date': 'str',
        'bill_package_number': 'str',
        'remarks': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'issue_date': 'issue_date',
        'due_date': 'due_date',
        'bill_status': 'bill_status',
        'bill_number': 'bill_number',
        'issuer_full_name': 'issuer_full_name',
        'issuer_account': 'issuer_account',
        'issuer_bank_name': 'issuer_bank_name',
        'issuer_bank_number': 'issuer_bank_number',
        'payee_full_name': 'payee_full_name',
        'payee_account': 'payee_account',
        'payee_bank_name': 'payee_bank_name',
        'payee_bank_number': 'payee_bank_number',
        'issuance_guarantor_name': 'issuance_guarantor_name',
        'issuance_guarantor_address': 'issuance_guarantor_address',
        'issuance_guarantor_account': 'issuance_guarantor_account',
        'issuance_guarantee_date': 'issuance_guarantee_date',
        'issuance_guarantor_bank_number': 'issuance_guarantor_bank_number',
        'issuance_guarantor_bank_name': 'issuance_guarantor_bank_name',
        'amount_in_words': 'amount_in_words',
        'amount_in_figures': 'amount_in_figures',
        'acceptor_full_name': 'acceptor_full_name',
        'acceptor_account': 'acceptor_account',
        'acceptor_bank_number': 'acceptor_bank_number',
        'acceptor_bank_name': 'acceptor_bank_name',
        'contract_number': 'contract_number',
        'assignability': 'assignability',
        'issuer_commitment': 'issuer_commitment',
        'acceptor_commitment': 'acceptor_commitment',
        'acceptance_date': 'acceptance_date',
        'acceptance_guarantor_name': 'acceptance_guarantor_name',
        'acceptance_guarantor_address': 'acceptance_guarantor_address',
        'acceptance_guarantor_account': 'acceptance_guarantor_account',
        'acceptance_guarantee_date': 'acceptance_guarantee_date',
        'acceptance_guarantor_bank_number': 'acceptance_guarantor_bank_number',
        'acceptance_guarantor_bank_name': 'acceptance_guarantor_bank_name',
        'issuer_rating_entity': 'issuer_rating_entity',
        'issuer_credit_rating': 'issuer_credit_rating',
        'issuer_rating_due_date': 'issuer_rating_due_date',
        'acceptor_rating_entity': 'acceptor_rating_entity',
        'acceptor_credit_rating': 'acceptor_credit_rating',
        'acceptor_rating_due_date': 'acceptor_rating_due_date',
        'bill_package_number': 'bill_package_number',
        'remarks': 'remarks',
        'confidence': 'confidence'
    }

    def __init__(self, issue_date=None, due_date=None, bill_status=None, bill_number=None, issuer_full_name=None, issuer_account=None, issuer_bank_name=None, issuer_bank_number=None, payee_full_name=None, payee_account=None, payee_bank_name=None, payee_bank_number=None, issuance_guarantor_name=None, issuance_guarantor_address=None, issuance_guarantor_account=None, issuance_guarantee_date=None, issuance_guarantor_bank_number=None, issuance_guarantor_bank_name=None, amount_in_words=None, amount_in_figures=None, acceptor_full_name=None, acceptor_account=None, acceptor_bank_number=None, acceptor_bank_name=None, contract_number=None, assignability=None, issuer_commitment=None, acceptor_commitment=None, acceptance_date=None, acceptance_guarantor_name=None, acceptance_guarantor_address=None, acceptance_guarantor_account=None, acceptance_guarantee_date=None, acceptance_guarantor_bank_number=None, acceptance_guarantor_bank_name=None, issuer_rating_entity=None, issuer_credit_rating=None, issuer_rating_due_date=None, acceptor_rating_entity=None, acceptor_credit_rating=None, acceptor_rating_due_date=None, bill_package_number=None, remarks=None, confidence=None):
        """AcceptanceBillResult

        The model defined in huaweicloud sdk

        :param issue_date: 出票日期。 
        :type issue_date: str
        :param due_date: 汇票到期日。 
        :type due_date: str
        :param bill_status: 票据状态。 
        :type bill_status: str
        :param bill_number: 票据号码。 
        :type bill_number: str
        :param issuer_full_name: 出票人全称。 
        :type issuer_full_name: str
        :param issuer_account: 出票人账号。 
        :type issuer_account: str
        :param issuer_bank_name: 出票人开户银行。 
        :type issuer_bank_name: str
        :param issuer_bank_number: 出票人开户行号。 
        :type issuer_bank_number: str
        :param payee_full_name: 收款人全称。 
        :type payee_full_name: str
        :param payee_account: 收款人账号。 
        :type payee_account: str
        :param payee_bank_name: 收款人开户银行。 
        :type payee_bank_name: str
        :param payee_bank_number: 收款人开户行号。 
        :type payee_bank_number: str
        :param issuance_guarantor_name: 出票保证人名称。 
        :type issuance_guarantor_name: str
        :param issuance_guarantor_address: 出票保证人地址。 
        :type issuance_guarantor_address: str
        :param issuance_guarantor_account: 出票保证人账号。 
        :type issuance_guarantor_account: str
        :param issuance_guarantee_date: 出票保证日期。 
        :type issuance_guarantee_date: str
        :param issuance_guarantor_bank_number: 出票保证人开户行行号。 
        :type issuance_guarantor_bank_number: str
        :param issuance_guarantor_bank_name: 出票保证人开户行名称。 
        :type issuance_guarantor_bank_name: str
        :param amount_in_words: 大写票据金额。 
        :type amount_in_words: str
        :param amount_in_figures: 小写票据金额。 
        :type amount_in_figures: str
        :param acceptor_full_name: 承兑人全称。 
        :type acceptor_full_name: str
        :param acceptor_account: 承兑人账号。 
        :type acceptor_account: str
        :param acceptor_bank_number: 承兑人开户行行号。 
        :type acceptor_bank_number: str
        :param acceptor_bank_name: 承兑人开户行名称。 
        :type acceptor_bank_name: str
        :param contract_number: 交易合同号。 
        :type contract_number: str
        :param assignability: 能否转让。 
        :type assignability: str
        :param issuer_commitment: 出票人承诺。 
        :type issuer_commitment: str
        :param acceptor_commitment: 承兑人承诺。 
        :type acceptor_commitment: str
        :param acceptance_date: 承兑日期。 
        :type acceptance_date: str
        :param acceptance_guarantor_name: 承兑保证人名称。 
        :type acceptance_guarantor_name: str
        :param acceptance_guarantor_address: 承兑保证人地址。 
        :type acceptance_guarantor_address: str
        :param acceptance_guarantor_account: 承兑保证人账号。 
        :type acceptance_guarantor_account: str
        :param acceptance_guarantee_date: 承兑保证日期。 
        :type acceptance_guarantee_date: str
        :param acceptance_guarantor_bank_number: 承兑保证人开户行行号。 
        :type acceptance_guarantor_bank_number: str
        :param acceptance_guarantor_bank_name: 承兑保证人开户行名称。 
        :type acceptance_guarantor_bank_name: str
        :param issuer_rating_entity: 出票人评级主体。 
        :type issuer_rating_entity: str
        :param issuer_credit_rating: 出票人信用等级。 
        :type issuer_credit_rating: str
        :param issuer_rating_due_date: 出票人评级到期日。 
        :type issuer_rating_due_date: str
        :param acceptor_rating_entity: 承兑人评级主体。 
        :type acceptor_rating_entity: str
        :param acceptor_credit_rating: 承兑人信用等级。 
        :type acceptor_credit_rating: str
        :param acceptor_rating_due_date: 承兑人评级到期日。 
        :type acceptor_rating_due_date: str
        :param bill_package_number: 票据包号。 
        :type bill_package_number: str
        :param remarks: 备注。   
        :type remarks: str
        :param confidence: 各个字段的置信度。 
        :type confidence: object
        """
        
        

        self._issue_date = None
        self._due_date = None
        self._bill_status = None
        self._bill_number = None
        self._issuer_full_name = None
        self._issuer_account = None
        self._issuer_bank_name = None
        self._issuer_bank_number = None
        self._payee_full_name = None
        self._payee_account = None
        self._payee_bank_name = None
        self._payee_bank_number = None
        self._issuance_guarantor_name = None
        self._issuance_guarantor_address = None
        self._issuance_guarantor_account = None
        self._issuance_guarantee_date = None
        self._issuance_guarantor_bank_number = None
        self._issuance_guarantor_bank_name = None
        self._amount_in_words = None
        self._amount_in_figures = None
        self._acceptor_full_name = None
        self._acceptor_account = None
        self._acceptor_bank_number = None
        self._acceptor_bank_name = None
        self._contract_number = None
        self._assignability = None
        self._issuer_commitment = None
        self._acceptor_commitment = None
        self._acceptance_date = None
        self._acceptance_guarantor_name = None
        self._acceptance_guarantor_address = None
        self._acceptance_guarantor_account = None
        self._acceptance_guarantee_date = None
        self._acceptance_guarantor_bank_number = None
        self._acceptance_guarantor_bank_name = None
        self._issuer_rating_entity = None
        self._issuer_credit_rating = None
        self._issuer_rating_due_date = None
        self._acceptor_rating_entity = None
        self._acceptor_credit_rating = None
        self._acceptor_rating_due_date = None
        self._bill_package_number = None
        self._remarks = None
        self._confidence = None
        self.discriminator = None

        if issue_date is not None:
            self.issue_date = issue_date
        if due_date is not None:
            self.due_date = due_date
        if bill_status is not None:
            self.bill_status = bill_status
        if bill_number is not None:
            self.bill_number = bill_number
        if issuer_full_name is not None:
            self.issuer_full_name = issuer_full_name
        if issuer_account is not None:
            self.issuer_account = issuer_account
        if issuer_bank_name is not None:
            self.issuer_bank_name = issuer_bank_name
        if issuer_bank_number is not None:
            self.issuer_bank_number = issuer_bank_number
        if payee_full_name is not None:
            self.payee_full_name = payee_full_name
        if payee_account is not None:
            self.payee_account = payee_account
        if payee_bank_name is not None:
            self.payee_bank_name = payee_bank_name
        if payee_bank_number is not None:
            self.payee_bank_number = payee_bank_number
        if issuance_guarantor_name is not None:
            self.issuance_guarantor_name = issuance_guarantor_name
        if issuance_guarantor_address is not None:
            self.issuance_guarantor_address = issuance_guarantor_address
        if issuance_guarantor_account is not None:
            self.issuance_guarantor_account = issuance_guarantor_account
        if issuance_guarantee_date is not None:
            self.issuance_guarantee_date = issuance_guarantee_date
        if issuance_guarantor_bank_number is not None:
            self.issuance_guarantor_bank_number = issuance_guarantor_bank_number
        if issuance_guarantor_bank_name is not None:
            self.issuance_guarantor_bank_name = issuance_guarantor_bank_name
        if amount_in_words is not None:
            self.amount_in_words = amount_in_words
        if amount_in_figures is not None:
            self.amount_in_figures = amount_in_figures
        if acceptor_full_name is not None:
            self.acceptor_full_name = acceptor_full_name
        if acceptor_account is not None:
            self.acceptor_account = acceptor_account
        if acceptor_bank_number is not None:
            self.acceptor_bank_number = acceptor_bank_number
        if acceptor_bank_name is not None:
            self.acceptor_bank_name = acceptor_bank_name
        if contract_number is not None:
            self.contract_number = contract_number
        if assignability is not None:
            self.assignability = assignability
        if issuer_commitment is not None:
            self.issuer_commitment = issuer_commitment
        if acceptor_commitment is not None:
            self.acceptor_commitment = acceptor_commitment
        if acceptance_date is not None:
            self.acceptance_date = acceptance_date
        if acceptance_guarantor_name is not None:
            self.acceptance_guarantor_name = acceptance_guarantor_name
        if acceptance_guarantor_address is not None:
            self.acceptance_guarantor_address = acceptance_guarantor_address
        if acceptance_guarantor_account is not None:
            self.acceptance_guarantor_account = acceptance_guarantor_account
        if acceptance_guarantee_date is not None:
            self.acceptance_guarantee_date = acceptance_guarantee_date
        if acceptance_guarantor_bank_number is not None:
            self.acceptance_guarantor_bank_number = acceptance_guarantor_bank_number
        if acceptance_guarantor_bank_name is not None:
            self.acceptance_guarantor_bank_name = acceptance_guarantor_bank_name
        if issuer_rating_entity is not None:
            self.issuer_rating_entity = issuer_rating_entity
        if issuer_credit_rating is not None:
            self.issuer_credit_rating = issuer_credit_rating
        if issuer_rating_due_date is not None:
            self.issuer_rating_due_date = issuer_rating_due_date
        if acceptor_rating_entity is not None:
            self.acceptor_rating_entity = acceptor_rating_entity
        if acceptor_credit_rating is not None:
            self.acceptor_credit_rating = acceptor_credit_rating
        if acceptor_rating_due_date is not None:
            self.acceptor_rating_due_date = acceptor_rating_due_date
        if bill_package_number is not None:
            self.bill_package_number = bill_package_number
        if remarks is not None:
            self.remarks = remarks
        if confidence is not None:
            self.confidence = confidence

    @property
    def issue_date(self):
        """Gets the issue_date of this AcceptanceBillResult.

        出票日期。 

        :return: The issue_date of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this AcceptanceBillResult.

        出票日期。 

        :param issue_date: The issue_date of this AcceptanceBillResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def due_date(self):
        """Gets the due_date of this AcceptanceBillResult.

        汇票到期日。 

        :return: The due_date of this AcceptanceBillResult.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this AcceptanceBillResult.

        汇票到期日。 

        :param due_date: The due_date of this AcceptanceBillResult.
        :type due_date: str
        """
        self._due_date = due_date

    @property
    def bill_status(self):
        """Gets the bill_status of this AcceptanceBillResult.

        票据状态。 

        :return: The bill_status of this AcceptanceBillResult.
        :rtype: str
        """
        return self._bill_status

    @bill_status.setter
    def bill_status(self, bill_status):
        """Sets the bill_status of this AcceptanceBillResult.

        票据状态。 

        :param bill_status: The bill_status of this AcceptanceBillResult.
        :type bill_status: str
        """
        self._bill_status = bill_status

    @property
    def bill_number(self):
        """Gets the bill_number of this AcceptanceBillResult.

        票据号码。 

        :return: The bill_number of this AcceptanceBillResult.
        :rtype: str
        """
        return self._bill_number

    @bill_number.setter
    def bill_number(self, bill_number):
        """Sets the bill_number of this AcceptanceBillResult.

        票据号码。 

        :param bill_number: The bill_number of this AcceptanceBillResult.
        :type bill_number: str
        """
        self._bill_number = bill_number

    @property
    def issuer_full_name(self):
        """Gets the issuer_full_name of this AcceptanceBillResult.

        出票人全称。 

        :return: The issuer_full_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuer_full_name

    @issuer_full_name.setter
    def issuer_full_name(self, issuer_full_name):
        """Sets the issuer_full_name of this AcceptanceBillResult.

        出票人全称。 

        :param issuer_full_name: The issuer_full_name of this AcceptanceBillResult.
        :type issuer_full_name: str
        """
        self._issuer_full_name = issuer_full_name

    @property
    def issuer_account(self):
        """Gets the issuer_account of this AcceptanceBillResult.

        出票人账号。 

        :return: The issuer_account of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuer_account

    @issuer_account.setter
    def issuer_account(self, issuer_account):
        """Sets the issuer_account of this AcceptanceBillResult.

        出票人账号。 

        :param issuer_account: The issuer_account of this AcceptanceBillResult.
        :type issuer_account: str
        """
        self._issuer_account = issuer_account

    @property
    def issuer_bank_name(self):
        """Gets the issuer_bank_name of this AcceptanceBillResult.

        出票人开户银行。 

        :return: The issuer_bank_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuer_bank_name

    @issuer_bank_name.setter
    def issuer_bank_name(self, issuer_bank_name):
        """Sets the issuer_bank_name of this AcceptanceBillResult.

        出票人开户银行。 

        :param issuer_bank_name: The issuer_bank_name of this AcceptanceBillResult.
        :type issuer_bank_name: str
        """
        self._issuer_bank_name = issuer_bank_name

    @property
    def issuer_bank_number(self):
        """Gets the issuer_bank_number of this AcceptanceBillResult.

        出票人开户行号。 

        :return: The issuer_bank_number of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuer_bank_number

    @issuer_bank_number.setter
    def issuer_bank_number(self, issuer_bank_number):
        """Sets the issuer_bank_number of this AcceptanceBillResult.

        出票人开户行号。 

        :param issuer_bank_number: The issuer_bank_number of this AcceptanceBillResult.
        :type issuer_bank_number: str
        """
        self._issuer_bank_number = issuer_bank_number

    @property
    def payee_full_name(self):
        """Gets the payee_full_name of this AcceptanceBillResult.

        收款人全称。 

        :return: The payee_full_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._payee_full_name

    @payee_full_name.setter
    def payee_full_name(self, payee_full_name):
        """Sets the payee_full_name of this AcceptanceBillResult.

        收款人全称。 

        :param payee_full_name: The payee_full_name of this AcceptanceBillResult.
        :type payee_full_name: str
        """
        self._payee_full_name = payee_full_name

    @property
    def payee_account(self):
        """Gets the payee_account of this AcceptanceBillResult.

        收款人账号。 

        :return: The payee_account of this AcceptanceBillResult.
        :rtype: str
        """
        return self._payee_account

    @payee_account.setter
    def payee_account(self, payee_account):
        """Sets the payee_account of this AcceptanceBillResult.

        收款人账号。 

        :param payee_account: The payee_account of this AcceptanceBillResult.
        :type payee_account: str
        """
        self._payee_account = payee_account

    @property
    def payee_bank_name(self):
        """Gets the payee_bank_name of this AcceptanceBillResult.

        收款人开户银行。 

        :return: The payee_bank_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._payee_bank_name

    @payee_bank_name.setter
    def payee_bank_name(self, payee_bank_name):
        """Sets the payee_bank_name of this AcceptanceBillResult.

        收款人开户银行。 

        :param payee_bank_name: The payee_bank_name of this AcceptanceBillResult.
        :type payee_bank_name: str
        """
        self._payee_bank_name = payee_bank_name

    @property
    def payee_bank_number(self):
        """Gets the payee_bank_number of this AcceptanceBillResult.

        收款人开户行号。 

        :return: The payee_bank_number of this AcceptanceBillResult.
        :rtype: str
        """
        return self._payee_bank_number

    @payee_bank_number.setter
    def payee_bank_number(self, payee_bank_number):
        """Sets the payee_bank_number of this AcceptanceBillResult.

        收款人开户行号。 

        :param payee_bank_number: The payee_bank_number of this AcceptanceBillResult.
        :type payee_bank_number: str
        """
        self._payee_bank_number = payee_bank_number

    @property
    def issuance_guarantor_name(self):
        """Gets the issuance_guarantor_name of this AcceptanceBillResult.

        出票保证人名称。 

        :return: The issuance_guarantor_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuance_guarantor_name

    @issuance_guarantor_name.setter
    def issuance_guarantor_name(self, issuance_guarantor_name):
        """Sets the issuance_guarantor_name of this AcceptanceBillResult.

        出票保证人名称。 

        :param issuance_guarantor_name: The issuance_guarantor_name of this AcceptanceBillResult.
        :type issuance_guarantor_name: str
        """
        self._issuance_guarantor_name = issuance_guarantor_name

    @property
    def issuance_guarantor_address(self):
        """Gets the issuance_guarantor_address of this AcceptanceBillResult.

        出票保证人地址。 

        :return: The issuance_guarantor_address of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuance_guarantor_address

    @issuance_guarantor_address.setter
    def issuance_guarantor_address(self, issuance_guarantor_address):
        """Sets the issuance_guarantor_address of this AcceptanceBillResult.

        出票保证人地址。 

        :param issuance_guarantor_address: The issuance_guarantor_address of this AcceptanceBillResult.
        :type issuance_guarantor_address: str
        """
        self._issuance_guarantor_address = issuance_guarantor_address

    @property
    def issuance_guarantor_account(self):
        """Gets the issuance_guarantor_account of this AcceptanceBillResult.

        出票保证人账号。 

        :return: The issuance_guarantor_account of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuance_guarantor_account

    @issuance_guarantor_account.setter
    def issuance_guarantor_account(self, issuance_guarantor_account):
        """Sets the issuance_guarantor_account of this AcceptanceBillResult.

        出票保证人账号。 

        :param issuance_guarantor_account: The issuance_guarantor_account of this AcceptanceBillResult.
        :type issuance_guarantor_account: str
        """
        self._issuance_guarantor_account = issuance_guarantor_account

    @property
    def issuance_guarantee_date(self):
        """Gets the issuance_guarantee_date of this AcceptanceBillResult.

        出票保证日期。 

        :return: The issuance_guarantee_date of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuance_guarantee_date

    @issuance_guarantee_date.setter
    def issuance_guarantee_date(self, issuance_guarantee_date):
        """Sets the issuance_guarantee_date of this AcceptanceBillResult.

        出票保证日期。 

        :param issuance_guarantee_date: The issuance_guarantee_date of this AcceptanceBillResult.
        :type issuance_guarantee_date: str
        """
        self._issuance_guarantee_date = issuance_guarantee_date

    @property
    def issuance_guarantor_bank_number(self):
        """Gets the issuance_guarantor_bank_number of this AcceptanceBillResult.

        出票保证人开户行行号。 

        :return: The issuance_guarantor_bank_number of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuance_guarantor_bank_number

    @issuance_guarantor_bank_number.setter
    def issuance_guarantor_bank_number(self, issuance_guarantor_bank_number):
        """Sets the issuance_guarantor_bank_number of this AcceptanceBillResult.

        出票保证人开户行行号。 

        :param issuance_guarantor_bank_number: The issuance_guarantor_bank_number of this AcceptanceBillResult.
        :type issuance_guarantor_bank_number: str
        """
        self._issuance_guarantor_bank_number = issuance_guarantor_bank_number

    @property
    def issuance_guarantor_bank_name(self):
        """Gets the issuance_guarantor_bank_name of this AcceptanceBillResult.

        出票保证人开户行名称。 

        :return: The issuance_guarantor_bank_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuance_guarantor_bank_name

    @issuance_guarantor_bank_name.setter
    def issuance_guarantor_bank_name(self, issuance_guarantor_bank_name):
        """Sets the issuance_guarantor_bank_name of this AcceptanceBillResult.

        出票保证人开户行名称。 

        :param issuance_guarantor_bank_name: The issuance_guarantor_bank_name of this AcceptanceBillResult.
        :type issuance_guarantor_bank_name: str
        """
        self._issuance_guarantor_bank_name = issuance_guarantor_bank_name

    @property
    def amount_in_words(self):
        """Gets the amount_in_words of this AcceptanceBillResult.

        大写票据金额。 

        :return: The amount_in_words of this AcceptanceBillResult.
        :rtype: str
        """
        return self._amount_in_words

    @amount_in_words.setter
    def amount_in_words(self, amount_in_words):
        """Sets the amount_in_words of this AcceptanceBillResult.

        大写票据金额。 

        :param amount_in_words: The amount_in_words of this AcceptanceBillResult.
        :type amount_in_words: str
        """
        self._amount_in_words = amount_in_words

    @property
    def amount_in_figures(self):
        """Gets the amount_in_figures of this AcceptanceBillResult.

        小写票据金额。 

        :return: The amount_in_figures of this AcceptanceBillResult.
        :rtype: str
        """
        return self._amount_in_figures

    @amount_in_figures.setter
    def amount_in_figures(self, amount_in_figures):
        """Sets the amount_in_figures of this AcceptanceBillResult.

        小写票据金额。 

        :param amount_in_figures: The amount_in_figures of this AcceptanceBillResult.
        :type amount_in_figures: str
        """
        self._amount_in_figures = amount_in_figures

    @property
    def acceptor_full_name(self):
        """Gets the acceptor_full_name of this AcceptanceBillResult.

        承兑人全称。 

        :return: The acceptor_full_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptor_full_name

    @acceptor_full_name.setter
    def acceptor_full_name(self, acceptor_full_name):
        """Sets the acceptor_full_name of this AcceptanceBillResult.

        承兑人全称。 

        :param acceptor_full_name: The acceptor_full_name of this AcceptanceBillResult.
        :type acceptor_full_name: str
        """
        self._acceptor_full_name = acceptor_full_name

    @property
    def acceptor_account(self):
        """Gets the acceptor_account of this AcceptanceBillResult.

        承兑人账号。 

        :return: The acceptor_account of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptor_account

    @acceptor_account.setter
    def acceptor_account(self, acceptor_account):
        """Sets the acceptor_account of this AcceptanceBillResult.

        承兑人账号。 

        :param acceptor_account: The acceptor_account of this AcceptanceBillResult.
        :type acceptor_account: str
        """
        self._acceptor_account = acceptor_account

    @property
    def acceptor_bank_number(self):
        """Gets the acceptor_bank_number of this AcceptanceBillResult.

        承兑人开户行行号。 

        :return: The acceptor_bank_number of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptor_bank_number

    @acceptor_bank_number.setter
    def acceptor_bank_number(self, acceptor_bank_number):
        """Sets the acceptor_bank_number of this AcceptanceBillResult.

        承兑人开户行行号。 

        :param acceptor_bank_number: The acceptor_bank_number of this AcceptanceBillResult.
        :type acceptor_bank_number: str
        """
        self._acceptor_bank_number = acceptor_bank_number

    @property
    def acceptor_bank_name(self):
        """Gets the acceptor_bank_name of this AcceptanceBillResult.

        承兑人开户行名称。 

        :return: The acceptor_bank_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptor_bank_name

    @acceptor_bank_name.setter
    def acceptor_bank_name(self, acceptor_bank_name):
        """Sets the acceptor_bank_name of this AcceptanceBillResult.

        承兑人开户行名称。 

        :param acceptor_bank_name: The acceptor_bank_name of this AcceptanceBillResult.
        :type acceptor_bank_name: str
        """
        self._acceptor_bank_name = acceptor_bank_name

    @property
    def contract_number(self):
        """Gets the contract_number of this AcceptanceBillResult.

        交易合同号。 

        :return: The contract_number of this AcceptanceBillResult.
        :rtype: str
        """
        return self._contract_number

    @contract_number.setter
    def contract_number(self, contract_number):
        """Sets the contract_number of this AcceptanceBillResult.

        交易合同号。 

        :param contract_number: The contract_number of this AcceptanceBillResult.
        :type contract_number: str
        """
        self._contract_number = contract_number

    @property
    def assignability(self):
        """Gets the assignability of this AcceptanceBillResult.

        能否转让。 

        :return: The assignability of this AcceptanceBillResult.
        :rtype: str
        """
        return self._assignability

    @assignability.setter
    def assignability(self, assignability):
        """Sets the assignability of this AcceptanceBillResult.

        能否转让。 

        :param assignability: The assignability of this AcceptanceBillResult.
        :type assignability: str
        """
        self._assignability = assignability

    @property
    def issuer_commitment(self):
        """Gets the issuer_commitment of this AcceptanceBillResult.

        出票人承诺。 

        :return: The issuer_commitment of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuer_commitment

    @issuer_commitment.setter
    def issuer_commitment(self, issuer_commitment):
        """Sets the issuer_commitment of this AcceptanceBillResult.

        出票人承诺。 

        :param issuer_commitment: The issuer_commitment of this AcceptanceBillResult.
        :type issuer_commitment: str
        """
        self._issuer_commitment = issuer_commitment

    @property
    def acceptor_commitment(self):
        """Gets the acceptor_commitment of this AcceptanceBillResult.

        承兑人承诺。 

        :return: The acceptor_commitment of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptor_commitment

    @acceptor_commitment.setter
    def acceptor_commitment(self, acceptor_commitment):
        """Sets the acceptor_commitment of this AcceptanceBillResult.

        承兑人承诺。 

        :param acceptor_commitment: The acceptor_commitment of this AcceptanceBillResult.
        :type acceptor_commitment: str
        """
        self._acceptor_commitment = acceptor_commitment

    @property
    def acceptance_date(self):
        """Gets the acceptance_date of this AcceptanceBillResult.

        承兑日期。 

        :return: The acceptance_date of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptance_date

    @acceptance_date.setter
    def acceptance_date(self, acceptance_date):
        """Sets the acceptance_date of this AcceptanceBillResult.

        承兑日期。 

        :param acceptance_date: The acceptance_date of this AcceptanceBillResult.
        :type acceptance_date: str
        """
        self._acceptance_date = acceptance_date

    @property
    def acceptance_guarantor_name(self):
        """Gets the acceptance_guarantor_name of this AcceptanceBillResult.

        承兑保证人名称。 

        :return: The acceptance_guarantor_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptance_guarantor_name

    @acceptance_guarantor_name.setter
    def acceptance_guarantor_name(self, acceptance_guarantor_name):
        """Sets the acceptance_guarantor_name of this AcceptanceBillResult.

        承兑保证人名称。 

        :param acceptance_guarantor_name: The acceptance_guarantor_name of this AcceptanceBillResult.
        :type acceptance_guarantor_name: str
        """
        self._acceptance_guarantor_name = acceptance_guarantor_name

    @property
    def acceptance_guarantor_address(self):
        """Gets the acceptance_guarantor_address of this AcceptanceBillResult.

        承兑保证人地址。 

        :return: The acceptance_guarantor_address of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptance_guarantor_address

    @acceptance_guarantor_address.setter
    def acceptance_guarantor_address(self, acceptance_guarantor_address):
        """Sets the acceptance_guarantor_address of this AcceptanceBillResult.

        承兑保证人地址。 

        :param acceptance_guarantor_address: The acceptance_guarantor_address of this AcceptanceBillResult.
        :type acceptance_guarantor_address: str
        """
        self._acceptance_guarantor_address = acceptance_guarantor_address

    @property
    def acceptance_guarantor_account(self):
        """Gets the acceptance_guarantor_account of this AcceptanceBillResult.

        承兑保证人账号。 

        :return: The acceptance_guarantor_account of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptance_guarantor_account

    @acceptance_guarantor_account.setter
    def acceptance_guarantor_account(self, acceptance_guarantor_account):
        """Sets the acceptance_guarantor_account of this AcceptanceBillResult.

        承兑保证人账号。 

        :param acceptance_guarantor_account: The acceptance_guarantor_account of this AcceptanceBillResult.
        :type acceptance_guarantor_account: str
        """
        self._acceptance_guarantor_account = acceptance_guarantor_account

    @property
    def acceptance_guarantee_date(self):
        """Gets the acceptance_guarantee_date of this AcceptanceBillResult.

        承兑保证日期。 

        :return: The acceptance_guarantee_date of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptance_guarantee_date

    @acceptance_guarantee_date.setter
    def acceptance_guarantee_date(self, acceptance_guarantee_date):
        """Sets the acceptance_guarantee_date of this AcceptanceBillResult.

        承兑保证日期。 

        :param acceptance_guarantee_date: The acceptance_guarantee_date of this AcceptanceBillResult.
        :type acceptance_guarantee_date: str
        """
        self._acceptance_guarantee_date = acceptance_guarantee_date

    @property
    def acceptance_guarantor_bank_number(self):
        """Gets the acceptance_guarantor_bank_number of this AcceptanceBillResult.

        承兑保证人开户行行号。 

        :return: The acceptance_guarantor_bank_number of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptance_guarantor_bank_number

    @acceptance_guarantor_bank_number.setter
    def acceptance_guarantor_bank_number(self, acceptance_guarantor_bank_number):
        """Sets the acceptance_guarantor_bank_number of this AcceptanceBillResult.

        承兑保证人开户行行号。 

        :param acceptance_guarantor_bank_number: The acceptance_guarantor_bank_number of this AcceptanceBillResult.
        :type acceptance_guarantor_bank_number: str
        """
        self._acceptance_guarantor_bank_number = acceptance_guarantor_bank_number

    @property
    def acceptance_guarantor_bank_name(self):
        """Gets the acceptance_guarantor_bank_name of this AcceptanceBillResult.

        承兑保证人开户行名称。 

        :return: The acceptance_guarantor_bank_name of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptance_guarantor_bank_name

    @acceptance_guarantor_bank_name.setter
    def acceptance_guarantor_bank_name(self, acceptance_guarantor_bank_name):
        """Sets the acceptance_guarantor_bank_name of this AcceptanceBillResult.

        承兑保证人开户行名称。 

        :param acceptance_guarantor_bank_name: The acceptance_guarantor_bank_name of this AcceptanceBillResult.
        :type acceptance_guarantor_bank_name: str
        """
        self._acceptance_guarantor_bank_name = acceptance_guarantor_bank_name

    @property
    def issuer_rating_entity(self):
        """Gets the issuer_rating_entity of this AcceptanceBillResult.

        出票人评级主体。 

        :return: The issuer_rating_entity of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuer_rating_entity

    @issuer_rating_entity.setter
    def issuer_rating_entity(self, issuer_rating_entity):
        """Sets the issuer_rating_entity of this AcceptanceBillResult.

        出票人评级主体。 

        :param issuer_rating_entity: The issuer_rating_entity of this AcceptanceBillResult.
        :type issuer_rating_entity: str
        """
        self._issuer_rating_entity = issuer_rating_entity

    @property
    def issuer_credit_rating(self):
        """Gets the issuer_credit_rating of this AcceptanceBillResult.

        出票人信用等级。 

        :return: The issuer_credit_rating of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuer_credit_rating

    @issuer_credit_rating.setter
    def issuer_credit_rating(self, issuer_credit_rating):
        """Sets the issuer_credit_rating of this AcceptanceBillResult.

        出票人信用等级。 

        :param issuer_credit_rating: The issuer_credit_rating of this AcceptanceBillResult.
        :type issuer_credit_rating: str
        """
        self._issuer_credit_rating = issuer_credit_rating

    @property
    def issuer_rating_due_date(self):
        """Gets the issuer_rating_due_date of this AcceptanceBillResult.

        出票人评级到期日。 

        :return: The issuer_rating_due_date of this AcceptanceBillResult.
        :rtype: str
        """
        return self._issuer_rating_due_date

    @issuer_rating_due_date.setter
    def issuer_rating_due_date(self, issuer_rating_due_date):
        """Sets the issuer_rating_due_date of this AcceptanceBillResult.

        出票人评级到期日。 

        :param issuer_rating_due_date: The issuer_rating_due_date of this AcceptanceBillResult.
        :type issuer_rating_due_date: str
        """
        self._issuer_rating_due_date = issuer_rating_due_date

    @property
    def acceptor_rating_entity(self):
        """Gets the acceptor_rating_entity of this AcceptanceBillResult.

        承兑人评级主体。 

        :return: The acceptor_rating_entity of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptor_rating_entity

    @acceptor_rating_entity.setter
    def acceptor_rating_entity(self, acceptor_rating_entity):
        """Sets the acceptor_rating_entity of this AcceptanceBillResult.

        承兑人评级主体。 

        :param acceptor_rating_entity: The acceptor_rating_entity of this AcceptanceBillResult.
        :type acceptor_rating_entity: str
        """
        self._acceptor_rating_entity = acceptor_rating_entity

    @property
    def acceptor_credit_rating(self):
        """Gets the acceptor_credit_rating of this AcceptanceBillResult.

        承兑人信用等级。 

        :return: The acceptor_credit_rating of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptor_credit_rating

    @acceptor_credit_rating.setter
    def acceptor_credit_rating(self, acceptor_credit_rating):
        """Sets the acceptor_credit_rating of this AcceptanceBillResult.

        承兑人信用等级。 

        :param acceptor_credit_rating: The acceptor_credit_rating of this AcceptanceBillResult.
        :type acceptor_credit_rating: str
        """
        self._acceptor_credit_rating = acceptor_credit_rating

    @property
    def acceptor_rating_due_date(self):
        """Gets the acceptor_rating_due_date of this AcceptanceBillResult.

        承兑人评级到期日。 

        :return: The acceptor_rating_due_date of this AcceptanceBillResult.
        :rtype: str
        """
        return self._acceptor_rating_due_date

    @acceptor_rating_due_date.setter
    def acceptor_rating_due_date(self, acceptor_rating_due_date):
        """Sets the acceptor_rating_due_date of this AcceptanceBillResult.

        承兑人评级到期日。 

        :param acceptor_rating_due_date: The acceptor_rating_due_date of this AcceptanceBillResult.
        :type acceptor_rating_due_date: str
        """
        self._acceptor_rating_due_date = acceptor_rating_due_date

    @property
    def bill_package_number(self):
        """Gets the bill_package_number of this AcceptanceBillResult.

        票据包号。 

        :return: The bill_package_number of this AcceptanceBillResult.
        :rtype: str
        """
        return self._bill_package_number

    @bill_package_number.setter
    def bill_package_number(self, bill_package_number):
        """Sets the bill_package_number of this AcceptanceBillResult.

        票据包号。 

        :param bill_package_number: The bill_package_number of this AcceptanceBillResult.
        :type bill_package_number: str
        """
        self._bill_package_number = bill_package_number

    @property
    def remarks(self):
        """Gets the remarks of this AcceptanceBillResult.

        备注。   

        :return: The remarks of this AcceptanceBillResult.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this AcceptanceBillResult.

        备注。   

        :param remarks: The remarks of this AcceptanceBillResult.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def confidence(self):
        """Gets the confidence of this AcceptanceBillResult.

        各个字段的置信度。 

        :return: The confidence of this AcceptanceBillResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this AcceptanceBillResult.

        各个字段的置信度。 

        :param confidence: The confidence of this AcceptanceBillResult.
        :type confidence: object
        """
        self._confidence = confidence

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AcceptanceBillResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
