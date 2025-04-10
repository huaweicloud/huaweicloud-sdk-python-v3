# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOptmJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'limit_concurrency': 'int'
    }

    attribute_map = {
        'id': 'id',
        'limit_concurrency': 'limit_concurrency'
    }

    def __init__(self, id=None, limit_concurrency=None):
        r"""CreateOptmJobResponse

        The model defined in huaweicloud sdk

        :param id: 作业id
        :type id: str
        :param limit_concurrency: 限制的并发量
        :type limit_concurrency: int
        """
        
        super(CreateOptmJobResponse, self).__init__()

        self._id = None
        self._limit_concurrency = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if limit_concurrency is not None:
            self.limit_concurrency = limit_concurrency

    @property
    def id(self):
        r"""Gets the id of this CreateOptmJobResponse.

        作业id

        :return: The id of this CreateOptmJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateOptmJobResponse.

        作业id

        :param id: The id of this CreateOptmJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def limit_concurrency(self):
        r"""Gets the limit_concurrency of this CreateOptmJobResponse.

        限制的并发量

        :return: The limit_concurrency of this CreateOptmJobResponse.
        :rtype: int
        """
        return self._limit_concurrency

    @limit_concurrency.setter
    def limit_concurrency(self, limit_concurrency):
        r"""Sets the limit_concurrency of this CreateOptmJobResponse.

        限制的并发量

        :param limit_concurrency: The limit_concurrency of this CreateOptmJobResponse.
        :type limit_concurrency: int
        """
        self._limit_concurrency = limit_concurrency

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
        if not isinstance(other, CreateOptmJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
