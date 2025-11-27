# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationComponentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'application_id': 'application_id',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, application_id=None, marker=None, limit=None):
        r"""ListApplicationComponentsRequest

        The model defined in huaweicloud sdk

        :param application_id: 应用id。
        :type application_id: str
        :param marker: 分页参数，上一页请求最后一个id。
        :type marker: str
        :param limit: 最大的返回数量。
        :type limit: int
        """
        
        

        self._application_id = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if marker is not None:
            self.marker = marker
        self.limit = limit

    @property
    def application_id(self):
        r"""Gets the application_id of this ListApplicationComponentsRequest.

        应用id。

        :return: The application_id of this ListApplicationComponentsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ListApplicationComponentsRequest.

        应用id。

        :param application_id: The application_id of this ListApplicationComponentsRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def marker(self):
        r"""Gets the marker of this ListApplicationComponentsRequest.

        分页参数，上一页请求最后一个id。

        :return: The marker of this ListApplicationComponentsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListApplicationComponentsRequest.

        分页参数，上一页请求最后一个id。

        :param marker: The marker of this ListApplicationComponentsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListApplicationComponentsRequest.

        最大的返回数量。

        :return: The limit of this ListApplicationComponentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListApplicationComponentsRequest.

        最大的返回数量。

        :param limit: The limit of this ListApplicationComponentsRequest.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListApplicationComponentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
