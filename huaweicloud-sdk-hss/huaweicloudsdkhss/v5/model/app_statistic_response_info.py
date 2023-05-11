# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppStatisticResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'num': 'int'
    }

    attribute_map = {
        'app_name': 'app_name',
        'num': 'num'
    }

    def __init__(self, app_name=None, num=None):
        """AppStatisticResponseInfo

        The model defined in huaweicloud sdk

        :param app_name: 软件名称
        :type app_name: str
        :param num: 进程数量
        :type num: int
        """
        
        

        self._app_name = None
        self._num = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if num is not None:
            self.num = num

    @property
    def app_name(self):
        """Gets the app_name of this AppStatisticResponseInfo.

        软件名称

        :return: The app_name of this AppStatisticResponseInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppStatisticResponseInfo.

        软件名称

        :param app_name: The app_name of this AppStatisticResponseInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def num(self):
        """Gets the num of this AppStatisticResponseInfo.

        进程数量

        :return: The num of this AppStatisticResponseInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this AppStatisticResponseInfo.

        进程数量

        :param num: The num of this AppStatisticResponseInfo.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, AppStatisticResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
