# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowManagedAccountTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manage_account_id': 'str',
        'account_id': 'str',
        'account_name': 'str',
        'blueprint_product_id': 'str',
        'blueprint_product_name': 'str',
        'blueprint_product_version': 'str',
        'blueprint_status': 'str',
        'blueprint_product_impl_type': 'str',
        'blueprint_product_impl_detail': 'str'
    }

    attribute_map = {
        'manage_account_id': 'manage_account_id',
        'account_id': 'account_id',
        'account_name': 'account_name',
        'blueprint_product_id': 'blueprint_product_id',
        'blueprint_product_name': 'blueprint_product_name',
        'blueprint_product_version': 'blueprint_product_version',
        'blueprint_status': 'blueprint_status',
        'blueprint_product_impl_type': 'blueprint_product_impl_type',
        'blueprint_product_impl_detail': 'blueprint_product_impl_detail'
    }

    def __init__(self, manage_account_id=None, account_id=None, account_name=None, blueprint_product_id=None, blueprint_product_name=None, blueprint_product_version=None, blueprint_status=None, blueprint_product_impl_type=None, blueprint_product_impl_detail=None):
        r"""ShowManagedAccountTemplateResponse

        The model defined in huaweicloud sdk

        :param manage_account_id: 管理员账号ID。
        :type manage_account_id: str
        :param account_id: 纳管账号ID。
        :type account_id: str
        :param account_name: 纳管账号名称。
        :type account_name: str
        :param blueprint_product_id: 模板ID。
        :type blueprint_product_id: str
        :param blueprint_product_name: 模板名称。
        :type blueprint_product_name: str
        :param blueprint_product_version: 模板版本。
        :type blueprint_product_version: str
        :param blueprint_status: 模板部署状态，包括失败, 完成, 进行中。
        :type blueprint_status: str
        :param blueprint_product_impl_type: 模板实现类型。
        :type blueprint_product_impl_type: str
        :param blueprint_product_impl_detail: 模板详情
        :type blueprint_product_impl_detail: str
        """
        
        super(ShowManagedAccountTemplateResponse, self).__init__()

        self._manage_account_id = None
        self._account_id = None
        self._account_name = None
        self._blueprint_product_id = None
        self._blueprint_product_name = None
        self._blueprint_product_version = None
        self._blueprint_status = None
        self._blueprint_product_impl_type = None
        self._blueprint_product_impl_detail = None
        self.discriminator = None

        if manage_account_id is not None:
            self.manage_account_id = manage_account_id
        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if blueprint_product_id is not None:
            self.blueprint_product_id = blueprint_product_id
        if blueprint_product_name is not None:
            self.blueprint_product_name = blueprint_product_name
        if blueprint_product_version is not None:
            self.blueprint_product_version = blueprint_product_version
        if blueprint_status is not None:
            self.blueprint_status = blueprint_status
        if blueprint_product_impl_type is not None:
            self.blueprint_product_impl_type = blueprint_product_impl_type
        if blueprint_product_impl_detail is not None:
            self.blueprint_product_impl_detail = blueprint_product_impl_detail

    @property
    def manage_account_id(self):
        r"""Gets the manage_account_id of this ShowManagedAccountTemplateResponse.

        管理员账号ID。

        :return: The manage_account_id of this ShowManagedAccountTemplateResponse.
        :rtype: str
        """
        return self._manage_account_id

    @manage_account_id.setter
    def manage_account_id(self, manage_account_id):
        r"""Sets the manage_account_id of this ShowManagedAccountTemplateResponse.

        管理员账号ID。

        :param manage_account_id: The manage_account_id of this ShowManagedAccountTemplateResponse.
        :type manage_account_id: str
        """
        self._manage_account_id = manage_account_id

    @property
    def account_id(self):
        r"""Gets the account_id of this ShowManagedAccountTemplateResponse.

        纳管账号ID。

        :return: The account_id of this ShowManagedAccountTemplateResponse.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ShowManagedAccountTemplateResponse.

        纳管账号ID。

        :param account_id: The account_id of this ShowManagedAccountTemplateResponse.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this ShowManagedAccountTemplateResponse.

        纳管账号名称。

        :return: The account_name of this ShowManagedAccountTemplateResponse.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this ShowManagedAccountTemplateResponse.

        纳管账号名称。

        :param account_name: The account_name of this ShowManagedAccountTemplateResponse.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def blueprint_product_id(self):
        r"""Gets the blueprint_product_id of this ShowManagedAccountTemplateResponse.

        模板ID。

        :return: The blueprint_product_id of this ShowManagedAccountTemplateResponse.
        :rtype: str
        """
        return self._blueprint_product_id

    @blueprint_product_id.setter
    def blueprint_product_id(self, blueprint_product_id):
        r"""Sets the blueprint_product_id of this ShowManagedAccountTemplateResponse.

        模板ID。

        :param blueprint_product_id: The blueprint_product_id of this ShowManagedAccountTemplateResponse.
        :type blueprint_product_id: str
        """
        self._blueprint_product_id = blueprint_product_id

    @property
    def blueprint_product_name(self):
        r"""Gets the blueprint_product_name of this ShowManagedAccountTemplateResponse.

        模板名称。

        :return: The blueprint_product_name of this ShowManagedAccountTemplateResponse.
        :rtype: str
        """
        return self._blueprint_product_name

    @blueprint_product_name.setter
    def blueprint_product_name(self, blueprint_product_name):
        r"""Sets the blueprint_product_name of this ShowManagedAccountTemplateResponse.

        模板名称。

        :param blueprint_product_name: The blueprint_product_name of this ShowManagedAccountTemplateResponse.
        :type blueprint_product_name: str
        """
        self._blueprint_product_name = blueprint_product_name

    @property
    def blueprint_product_version(self):
        r"""Gets the blueprint_product_version of this ShowManagedAccountTemplateResponse.

        模板版本。

        :return: The blueprint_product_version of this ShowManagedAccountTemplateResponse.
        :rtype: str
        """
        return self._blueprint_product_version

    @blueprint_product_version.setter
    def blueprint_product_version(self, blueprint_product_version):
        r"""Sets the blueprint_product_version of this ShowManagedAccountTemplateResponse.

        模板版本。

        :param blueprint_product_version: The blueprint_product_version of this ShowManagedAccountTemplateResponse.
        :type blueprint_product_version: str
        """
        self._blueprint_product_version = blueprint_product_version

    @property
    def blueprint_status(self):
        r"""Gets the blueprint_status of this ShowManagedAccountTemplateResponse.

        模板部署状态，包括失败, 完成, 进行中。

        :return: The blueprint_status of this ShowManagedAccountTemplateResponse.
        :rtype: str
        """
        return self._blueprint_status

    @blueprint_status.setter
    def blueprint_status(self, blueprint_status):
        r"""Sets the blueprint_status of this ShowManagedAccountTemplateResponse.

        模板部署状态，包括失败, 完成, 进行中。

        :param blueprint_status: The blueprint_status of this ShowManagedAccountTemplateResponse.
        :type blueprint_status: str
        """
        self._blueprint_status = blueprint_status

    @property
    def blueprint_product_impl_type(self):
        r"""Gets the blueprint_product_impl_type of this ShowManagedAccountTemplateResponse.

        模板实现类型。

        :return: The blueprint_product_impl_type of this ShowManagedAccountTemplateResponse.
        :rtype: str
        """
        return self._blueprint_product_impl_type

    @blueprint_product_impl_type.setter
    def blueprint_product_impl_type(self, blueprint_product_impl_type):
        r"""Sets the blueprint_product_impl_type of this ShowManagedAccountTemplateResponse.

        模板实现类型。

        :param blueprint_product_impl_type: The blueprint_product_impl_type of this ShowManagedAccountTemplateResponse.
        :type blueprint_product_impl_type: str
        """
        self._blueprint_product_impl_type = blueprint_product_impl_type

    @property
    def blueprint_product_impl_detail(self):
        r"""Gets the blueprint_product_impl_detail of this ShowManagedAccountTemplateResponse.

        模板详情

        :return: The blueprint_product_impl_detail of this ShowManagedAccountTemplateResponse.
        :rtype: str
        """
        return self._blueprint_product_impl_detail

    @blueprint_product_impl_detail.setter
    def blueprint_product_impl_detail(self, blueprint_product_impl_detail):
        r"""Sets the blueprint_product_impl_detail of this ShowManagedAccountTemplateResponse.

        模板详情

        :param blueprint_product_impl_detail: The blueprint_product_impl_detail of this ShowManagedAccountTemplateResponse.
        :type blueprint_product_impl_detail: str
        """
        self._blueprint_product_impl_detail = blueprint_product_impl_detail

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
        if not isinstance(other, ShowManagedAccountTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
