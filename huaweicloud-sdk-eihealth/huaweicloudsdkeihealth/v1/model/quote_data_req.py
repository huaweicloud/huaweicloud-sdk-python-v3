# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuoteDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quote_project_id': 'str',
        'sub_paths': 'list[str]'
    }

    attribute_map = {
        'quote_project_id': 'quote_project_id',
        'sub_paths': 'sub_paths'
    }

    def __init__(self, quote_project_id=None, sub_paths=None):
        """QuoteDataReq

        The model defined in huaweicloud sdk

        :param quote_project_id: 引入项目ID
        :type quote_project_id: str
        :param sub_paths: 引入路径集
        :type sub_paths: list[str]
        """
        
        

        self._quote_project_id = None
        self._sub_paths = None
        self.discriminator = None

        self.quote_project_id = quote_project_id
        self.sub_paths = sub_paths

    @property
    def quote_project_id(self):
        """Gets the quote_project_id of this QuoteDataReq.

        引入项目ID

        :return: The quote_project_id of this QuoteDataReq.
        :rtype: str
        """
        return self._quote_project_id

    @quote_project_id.setter
    def quote_project_id(self, quote_project_id):
        """Sets the quote_project_id of this QuoteDataReq.

        引入项目ID

        :param quote_project_id: The quote_project_id of this QuoteDataReq.
        :type quote_project_id: str
        """
        self._quote_project_id = quote_project_id

    @property
    def sub_paths(self):
        """Gets the sub_paths of this QuoteDataReq.

        引入路径集

        :return: The sub_paths of this QuoteDataReq.
        :rtype: list[str]
        """
        return self._sub_paths

    @sub_paths.setter
    def sub_paths(self, sub_paths):
        """Sets the sub_paths of this QuoteDataReq.

        引入路径集

        :param sub_paths: The sub_paths of this QuoteDataReq.
        :type sub_paths: list[str]
        """
        self._sub_paths = sub_paths

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
        if not isinstance(other, QuoteDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
