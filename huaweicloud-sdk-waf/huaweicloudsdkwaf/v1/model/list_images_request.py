# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'atlas_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str'
    }

    attribute_map = {
        'atlas_id': 'atlas_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name'
    }

    def __init__(self, atlas_id=None, offset=None, limit=None, name=None):
        r"""ListImagesRequest

        The model defined in huaweicloud sdk

        :param atlas_id: 图库ID
        :type atlas_id: str
        :param offset: 分页偏移量，默认0
        :type offset: int
        :param limit: 每页条数，1~1000，默认10
        :type limit: int
        :param name: 图片名称（模糊匹配）
        :type name: str
        """
        
        

        self._atlas_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self.discriminator = None

        self.atlas_id = atlas_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name

    @property
    def atlas_id(self):
        r"""Gets the atlas_id of this ListImagesRequest.

        图库ID

        :return: The atlas_id of this ListImagesRequest.
        :rtype: str
        """
        return self._atlas_id

    @atlas_id.setter
    def atlas_id(self, atlas_id):
        r"""Sets the atlas_id of this ListImagesRequest.

        图库ID

        :param atlas_id: The atlas_id of this ListImagesRequest.
        :type atlas_id: str
        """
        self._atlas_id = atlas_id

    @property
    def offset(self):
        r"""Gets the offset of this ListImagesRequest.

        分页偏移量，默认0

        :return: The offset of this ListImagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImagesRequest.

        分页偏移量，默认0

        :param offset: The offset of this ListImagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImagesRequest.

        每页条数，1~1000，默认10

        :return: The limit of this ListImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImagesRequest.

        每页条数，1~1000，默认10

        :param limit: The limit of this ListImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListImagesRequest.

        图片名称（模糊匹配）

        :return: The name of this ListImagesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListImagesRequest.

        图片名称（模糊匹配）

        :param name: The name of this ListImagesRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
