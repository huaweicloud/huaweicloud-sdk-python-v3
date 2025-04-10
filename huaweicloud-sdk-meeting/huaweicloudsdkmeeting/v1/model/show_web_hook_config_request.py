# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWebHookConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'corp_id': 'str',
        'sp_id': 'str'
    }

    attribute_map = {
        'corp_id': 'corpId',
        'sp_id': 'spId'
    }

    def __init__(self, corp_id=None, sp_id=None):
        r"""ShowWebHookConfigRequest

        The model defined in huaweicloud sdk

        :param corp_id: 企业ID。按企业注册回调时需要填写。
        :type corp_id: str
        :param sp_id: SP ID。多租户场景下，按SP注册回调时需要填写。
        :type sp_id: str
        """
        
        

        self._corp_id = None
        self._sp_id = None
        self.discriminator = None

        if corp_id is not None:
            self.corp_id = corp_id
        if sp_id is not None:
            self.sp_id = sp_id

    @property
    def corp_id(self):
        r"""Gets the corp_id of this ShowWebHookConfigRequest.

        企业ID。按企业注册回调时需要填写。

        :return: The corp_id of this ShowWebHookConfigRequest.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        r"""Sets the corp_id of this ShowWebHookConfigRequest.

        企业ID。按企业注册回调时需要填写。

        :param corp_id: The corp_id of this ShowWebHookConfigRequest.
        :type corp_id: str
        """
        self._corp_id = corp_id

    @property
    def sp_id(self):
        r"""Gets the sp_id of this ShowWebHookConfigRequest.

        SP ID。多租户场景下，按SP注册回调时需要填写。

        :return: The sp_id of this ShowWebHookConfigRequest.
        :rtype: str
        """
        return self._sp_id

    @sp_id.setter
    def sp_id(self, sp_id):
        r"""Sets the sp_id of this ShowWebHookConfigRequest.

        SP ID。多租户场景下，按SP注册回调时需要填写。

        :param sp_id: The sp_id of this ShowWebHookConfigRequest.
        :type sp_id: str
        """
        self._sp_id = sp_id

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
        if not isinstance(other, ShowWebHookConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
