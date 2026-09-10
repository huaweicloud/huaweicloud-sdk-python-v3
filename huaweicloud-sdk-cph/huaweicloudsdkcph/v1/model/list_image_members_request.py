# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'image_id': 'image_id',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, image_id=None, marker=None, limit=None):
        r"""ListImageMembersRequest

        The model defined in huaweicloud sdk

        :param image_id: 镜像id。
        :type image_id: str
        :param marker: 分页标记。
        :type marker: str
        :param limit: 每页返回的共享账号个数。取值范围：1~100（默认值为100），一般设置为10、20、50。
        :type limit: int
        """
        
        

        self._image_id = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.image_id = image_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def image_id(self):
        r"""Gets the image_id of this ListImageMembersRequest.

        镜像id。

        :return: The image_id of this ListImageMembersRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListImageMembersRequest.

        镜像id。

        :param image_id: The image_id of this ListImageMembersRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def marker(self):
        r"""Gets the marker of this ListImageMembersRequest.

        分页标记。

        :return: The marker of this ListImageMembersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListImageMembersRequest.

        分页标记。

        :param marker: The marker of this ListImageMembersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListImageMembersRequest.

        每页返回的共享账号个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :return: The limit of this ListImageMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageMembersRequest.

        每页返回的共享账号个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :param limit: The limit of this ListImageMembersRequest.
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
        if not isinstance(other, ListImageMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
