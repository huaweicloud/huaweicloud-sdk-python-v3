# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhoneImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_type': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'image_type': 'image_type',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, image_type=None, marker=None, limit=None):
        r"""ListCloudPhoneImagesRequest

        The model defined in huaweicloud sdk

        :param image_type: 镜像类型 公共镜像：public 私有镜像：private 共享镜像：share 所有类型镜像：all
        :type image_type: str
        :param marker: 分页标记。
        :type marker: str
        :param limit: 每页返回的镜像个数。取值范围：1~500（默认值为500），一般设置为10、20、50。 当image_type传all时，分页返回顺序按公共镜像：public 私有镜像，private 共享镜像：share
        :type limit: int
        """
        
        

        self._image_type = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if image_type is not None:
            self.image_type = image_type
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def image_type(self):
        r"""Gets the image_type of this ListCloudPhoneImagesRequest.

        镜像类型 公共镜像：public 私有镜像：private 共享镜像：share 所有类型镜像：all

        :return: The image_type of this ListCloudPhoneImagesRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListCloudPhoneImagesRequest.

        镜像类型 公共镜像：public 私有镜像：private 共享镜像：share 所有类型镜像：all

        :param image_type: The image_type of this ListCloudPhoneImagesRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def marker(self):
        r"""Gets the marker of this ListCloudPhoneImagesRequest.

        分页标记。

        :return: The marker of this ListCloudPhoneImagesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCloudPhoneImagesRequest.

        分页标记。

        :param marker: The marker of this ListCloudPhoneImagesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListCloudPhoneImagesRequest.

        每页返回的镜像个数。取值范围：1~500（默认值为500），一般设置为10、20、50。 当image_type传all时，分页返回顺序按公共镜像：public 私有镜像，private 共享镜像：share

        :return: The limit of this ListCloudPhoneImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCloudPhoneImagesRequest.

        每页返回的镜像个数。取值范围：1~500（默认值为500），一般设置为10、20、50。 当image_type传all时，分页返回顺序按公共镜像：public 私有镜像，private 共享镜像：share

        :param limit: The limit of this ListCloudPhoneImagesRequest.
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
        if not isinstance(other, ListCloudPhoneImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
