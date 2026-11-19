# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyGroupDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'support_version': 'str',
        'support_os': 'str',
        'data_list': 'list[ShowPolicyDetailResponseInfo]'
    }

    attribute_map = {
        'description': 'description',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'support_version': 'support_version',
        'support_os': 'support_os',
        'data_list': 'data_list'
    }

    def __init__(self, description=None, group_id=None, group_name=None, support_version=None, support_os=None, data_list=None):
        r"""ListPolicyGroupDetailResponse

        The model defined in huaweicloud sdk

        :param description: **参数解释**： 策略组描述 **取值范围**： 字符长度1-64位 
        :type description: str
        :param group_id: **参数解释**： 策略组ID **取值范围**： 字符长度1-128位 
        :type group_id: str
        :param group_name: **参数解释**： 策略组名称 **取值范围**： 字符长度1-256位 
        :type group_name: str
        :param support_version: **参数解释**： 支持的版本 **取值范围**： 字符长度1-64位 
        :type support_version: str
        :param support_os: **参数解释**： 支持的操作系统 **取值范围**： 字符长度1-64位 
        :type support_os: str
        :param data_list: **参数解释**： 策略详情列表 **取值范围**： 不涉及 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ShowPolicyDetailResponseInfo`]
        """
        
        super().__init__()

        self._description = None
        self._group_id = None
        self._group_name = None
        self._support_version = None
        self._support_os = None
        self._data_list = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if support_version is not None:
            self.support_version = support_version
        if support_os is not None:
            self.support_os = support_os
        if data_list is not None:
            self.data_list = data_list

    @property
    def description(self):
        r"""Gets the description of this ListPolicyGroupDetailResponse.

        **参数解释**： 策略组描述 **取值范围**： 字符长度1-64位 

        :return: The description of this ListPolicyGroupDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListPolicyGroupDetailResponse.

        **参数解释**： 策略组描述 **取值范围**： 字符长度1-64位 

        :param description: The description of this ListPolicyGroupDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def group_id(self):
        r"""Gets the group_id of this ListPolicyGroupDetailResponse.

        **参数解释**： 策略组ID **取值范围**： 字符长度1-128位 

        :return: The group_id of this ListPolicyGroupDetailResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListPolicyGroupDetailResponse.

        **参数解释**： 策略组ID **取值范围**： 字符长度1-128位 

        :param group_id: The group_id of this ListPolicyGroupDetailResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ListPolicyGroupDetailResponse.

        **参数解释**： 策略组名称 **取值范围**： 字符长度1-256位 

        :return: The group_name of this ListPolicyGroupDetailResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListPolicyGroupDetailResponse.

        **参数解释**： 策略组名称 **取值范围**： 字符长度1-256位 

        :param group_name: The group_name of this ListPolicyGroupDetailResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def support_version(self):
        r"""Gets the support_version of this ListPolicyGroupDetailResponse.

        **参数解释**： 支持的版本 **取值范围**： 字符长度1-64位 

        :return: The support_version of this ListPolicyGroupDetailResponse.
        :rtype: str
        """
        return self._support_version

    @support_version.setter
    def support_version(self, support_version):
        r"""Sets the support_version of this ListPolicyGroupDetailResponse.

        **参数解释**： 支持的版本 **取值范围**： 字符长度1-64位 

        :param support_version: The support_version of this ListPolicyGroupDetailResponse.
        :type support_version: str
        """
        self._support_version = support_version

    @property
    def support_os(self):
        r"""Gets the support_os of this ListPolicyGroupDetailResponse.

        **参数解释**： 支持的操作系统 **取值范围**： 字符长度1-64位 

        :return: The support_os of this ListPolicyGroupDetailResponse.
        :rtype: str
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        r"""Sets the support_os of this ListPolicyGroupDetailResponse.

        **参数解释**： 支持的操作系统 **取值范围**： 字符长度1-64位 

        :param support_os: The support_os of this ListPolicyGroupDetailResponse.
        :type support_os: str
        """
        self._support_os = support_os

    @property
    def data_list(self):
        r"""Gets the data_list of this ListPolicyGroupDetailResponse.

        **参数解释**： 策略详情列表 **取值范围**： 不涉及 

        :return: The data_list of this ListPolicyGroupDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ShowPolicyDetailResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListPolicyGroupDetailResponse.

        **参数解释**： 策略详情列表 **取值范围**： 不涉及 

        :param data_list: The data_list of this ListPolicyGroupDetailResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ShowPolicyDetailResponseInfo`]
        """
        self._data_list = data_list

    def to_dict(self):
        import warnings
        warnings.warn("ListPolicyGroupDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListPolicyGroupDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
