# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransactionConfigSearchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_id': 'int',
        'env_id': 'int',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'business_id': 'business_id',
        'env_id': 'env_id',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, business_id=None, env_id=None, page_no=None, page_size=None):
        """TransactionConfigSearchRequest

        The model defined in huaweicloud sdk

        :param business_id: 应用id。
        :type business_id: int
        :param env_id: 环境id。
        :type env_id: int
        :param page_no: 页码。
        :type page_no: int
        :param page_size: 每页数量。
        :type page_size: int
        """
        
        

        self._business_id = None
        self._env_id = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        self.business_id = business_id
        if env_id is not None:
            self.env_id = env_id
        self.page_no = page_no
        self.page_size = page_size

    @property
    def business_id(self):
        """Gets the business_id of this TransactionConfigSearchRequest.

        应用id。

        :return: The business_id of this TransactionConfigSearchRequest.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this TransactionConfigSearchRequest.

        应用id。

        :param business_id: The business_id of this TransactionConfigSearchRequest.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def env_id(self):
        """Gets the env_id of this TransactionConfigSearchRequest.

        环境id。

        :return: The env_id of this TransactionConfigSearchRequest.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this TransactionConfigSearchRequest.

        环境id。

        :param env_id: The env_id of this TransactionConfigSearchRequest.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def page_no(self):
        """Gets the page_no of this TransactionConfigSearchRequest.

        页码。

        :return: The page_no of this TransactionConfigSearchRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this TransactionConfigSearchRequest.

        页码。

        :param page_no: The page_no of this TransactionConfigSearchRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this TransactionConfigSearchRequest.

        每页数量。

        :return: The page_size of this TransactionConfigSearchRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this TransactionConfigSearchRequest.

        每页数量。

        :param page_size: The page_size of this TransactionConfigSearchRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, TransactionConfigSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
