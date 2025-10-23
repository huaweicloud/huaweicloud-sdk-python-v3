# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportSettingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'setting_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'setting_id': 'setting_id'
    }

    def __init__(self, domain_id=None, setting_id=None):
        r"""ShowReportSettingRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param setting_id: 报告配置ID
        :type setting_id: str
        """
        
        

        self._domain_id = None
        self._setting_id = None
        self.discriminator = None

        self.domain_id = domain_id
        self.setting_id = setting_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowReportSettingRequest.

        账号ID

        :return: The domain_id of this ShowReportSettingRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowReportSettingRequest.

        账号ID

        :param domain_id: The domain_id of this ShowReportSettingRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def setting_id(self):
        r"""Gets the setting_id of this ShowReportSettingRequest.

        报告配置ID

        :return: The setting_id of this ShowReportSettingRequest.
        :rtype: str
        """
        return self._setting_id

    @setting_id.setter
    def setting_id(self, setting_id):
        r"""Sets the setting_id of this ShowReportSettingRequest.

        报告配置ID

        :param setting_id: The setting_id of this ShowReportSettingRequest.
        :type setting_id: str
        """
        self._setting_id = setting_id

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
        if not isinstance(other, ShowReportSettingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
