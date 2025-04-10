# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppQuotaBindingApp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_ids': 'list[str]'
    }

    attribute_map = {
        'app_ids': 'app_ids'
    }

    def __init__(self, app_ids=None):
        r"""CreateAppQuotaBindingApp

        The model defined in huaweicloud sdk

        :param app_ids: 凭据编号列表
        :type app_ids: list[str]
        """
        
        

        self._app_ids = None
        self.discriminator = None

        self.app_ids = app_ids

    @property
    def app_ids(self):
        r"""Gets the app_ids of this CreateAppQuotaBindingApp.

        凭据编号列表

        :return: The app_ids of this CreateAppQuotaBindingApp.
        :rtype: list[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        r"""Sets the app_ids of this CreateAppQuotaBindingApp.

        凭据编号列表

        :param app_ids: The app_ids of this CreateAppQuotaBindingApp.
        :type app_ids: list[str]
        """
        self._app_ids = app_ids

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
        if not isinstance(other, CreateAppQuotaBindingApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
