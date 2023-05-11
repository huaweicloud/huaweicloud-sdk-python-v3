# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppQuotaAppBinding:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_quota_id': 'str',
        'app_id': 'str',
        'bound_time': 'datetime'
    }

    attribute_map = {
        'app_quota_id': 'app_quota_id',
        'app_id': 'app_id',
        'bound_time': 'bound_time'
    }

    def __init__(self, app_quota_id=None, app_id=None, bound_time=None):
        """AppQuotaAppBinding

        The model defined in huaweicloud sdk

        :param app_quota_id: 客户端配额编号
        :type app_quota_id: str
        :param app_id: 客户端应用编号
        :type app_id: str
        :param bound_time: 绑定时间
        :type bound_time: datetime
        """
        
        

        self._app_quota_id = None
        self._app_id = None
        self._bound_time = None
        self.discriminator = None

        if app_quota_id is not None:
            self.app_quota_id = app_quota_id
        if app_id is not None:
            self.app_id = app_id
        if bound_time is not None:
            self.bound_time = bound_time

    @property
    def app_quota_id(self):
        """Gets the app_quota_id of this AppQuotaAppBinding.

        客户端配额编号

        :return: The app_quota_id of this AppQuotaAppBinding.
        :rtype: str
        """
        return self._app_quota_id

    @app_quota_id.setter
    def app_quota_id(self, app_quota_id):
        """Sets the app_quota_id of this AppQuotaAppBinding.

        客户端配额编号

        :param app_quota_id: The app_quota_id of this AppQuotaAppBinding.
        :type app_quota_id: str
        """
        self._app_quota_id = app_quota_id

    @property
    def app_id(self):
        """Gets the app_id of this AppQuotaAppBinding.

        客户端应用编号

        :return: The app_id of this AppQuotaAppBinding.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppQuotaAppBinding.

        客户端应用编号

        :param app_id: The app_id of this AppQuotaAppBinding.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def bound_time(self):
        """Gets the bound_time of this AppQuotaAppBinding.

        绑定时间

        :return: The bound_time of this AppQuotaAppBinding.
        :rtype: datetime
        """
        return self._bound_time

    @bound_time.setter
    def bound_time(self, bound_time):
        """Sets the bound_time of this AppQuotaAppBinding.

        绑定时间

        :param bound_time: The bound_time of this AppQuotaAppBinding.
        :type bound_time: datetime
        """
        self._bound_time = bound_time

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
        if not isinstance(other, AppQuotaAppBinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
