# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSpaceAnalysisTaskBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate': 'str',
        'datastore_type': 'str'
    }

    attribute_map = {
        'operate': 'operate',
        'datastore_type': 'datastore_type'
    }

    def __init__(self, operate=None, datastore_type=None):
        """CreateSpaceAnalysisTaskBody

        The model defined in huaweicloud sdk

        :param operate: 操作类型
        :type operate: str
        :param datastore_type: 引擎类型
        :type datastore_type: str
        """
        
        

        self._operate = None
        self._datastore_type = None
        self.discriminator = None

        self.operate = operate
        self.datastore_type = datastore_type

    @property
    def operate(self):
        """Gets the operate of this CreateSpaceAnalysisTaskBody.

        操作类型

        :return: The operate of this CreateSpaceAnalysisTaskBody.
        :rtype: str
        """
        return self._operate

    @operate.setter
    def operate(self, operate):
        """Sets the operate of this CreateSpaceAnalysisTaskBody.

        操作类型

        :param operate: The operate of this CreateSpaceAnalysisTaskBody.
        :type operate: str
        """
        self._operate = operate

    @property
    def datastore_type(self):
        """Gets the datastore_type of this CreateSpaceAnalysisTaskBody.

        引擎类型

        :return: The datastore_type of this CreateSpaceAnalysisTaskBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this CreateSpaceAnalysisTaskBody.

        引擎类型

        :param datastore_type: The datastore_type of this CreateSpaceAnalysisTaskBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

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
        if not isinstance(other, CreateSpaceAnalysisTaskBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
