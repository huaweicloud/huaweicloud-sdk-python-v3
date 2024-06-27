# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_id': 'str',
        'script_url': 'str'
    }

    attribute_map = {
        'case_id': 'case_id',
        'script_url': 'script_url'
    }

    def __init__(self, case_id=None, script_url=None):
        """CaseInfo

        The model defined in huaweicloud sdk

        :param case_id: 用例id
        :type case_id: str
        :param script_url: 脚本路径
        :type script_url: str
        """
        
        

        self._case_id = None
        self._script_url = None
        self.discriminator = None

        if case_id is not None:
            self.case_id = case_id
        if script_url is not None:
            self.script_url = script_url

    @property
    def case_id(self):
        """Gets the case_id of this CaseInfo.

        用例id

        :return: The case_id of this CaseInfo.
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        """Sets the case_id of this CaseInfo.

        用例id

        :param case_id: The case_id of this CaseInfo.
        :type case_id: str
        """
        self._case_id = case_id

    @property
    def script_url(self):
        """Gets the script_url of this CaseInfo.

        脚本路径

        :return: The script_url of this CaseInfo.
        :rtype: str
        """
        return self._script_url

    @script_url.setter
    def script_url(self, script_url):
        """Sets the script_url of this CaseInfo.

        脚本路径

        :param script_url: The script_url of this CaseInfo.
        :type script_url: str
        """
        self._script_url = script_url

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
        if not isinstance(other, CaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
