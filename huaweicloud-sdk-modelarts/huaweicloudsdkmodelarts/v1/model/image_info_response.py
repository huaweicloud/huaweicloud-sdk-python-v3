# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageInfoResponse:

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
        'source': 'str',
        'swr_path': 'str',
        'category': 'str'
    }

    attribute_map = {
        'id': 'id',
        'source': 'source',
        'swr_path': 'swr_path',
        'category': 'category'
    }

    def __init__(self, id=None, source=None, swr_path=None, category=None):
        r"""ImageInfoResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 镜像id。 **取值范围：** 不涉及。
        :type id: str
        :param source: **参数解释：** 镜像类别，标识镜像来源。 **取值范围：** - SWR：软件仓库服务。
        :type source: str
        :param swr_path: **参数解释：** 镜像地址，source不同取值时，地址为不同值。 **取值范围：** 不涉及。
        :type swr_path: str
        :param category: **参数解释：** 镜像支持的规格。 **取值范围：** - GPU：图形处理器。 - CPU：中央处理器。 - ASCEND：昇腾芯片。
        :type category: str
        """
        
        

        self._id = None
        self._source = None
        self._swr_path = None
        self._category = None
        self.discriminator = None

        self.id = id
        self.source = source
        self.swr_path = swr_path
        if category is not None:
            self.category = category

    @property
    def id(self):
        r"""Gets the id of this ImageInfoResponse.

        **参数解释：** 镜像id。 **取值范围：** 不涉及。

        :return: The id of this ImageInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageInfoResponse.

        **参数解释：** 镜像id。 **取值范围：** 不涉及。

        :param id: The id of this ImageInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def source(self):
        r"""Gets the source of this ImageInfoResponse.

        **参数解释：** 镜像类别，标识镜像来源。 **取值范围：** - SWR：软件仓库服务。

        :return: The source of this ImageInfoResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ImageInfoResponse.

        **参数解释：** 镜像类别，标识镜像来源。 **取值范围：** - SWR：软件仓库服务。

        :param source: The source of this ImageInfoResponse.
        :type source: str
        """
        self._source = source

    @property
    def swr_path(self):
        r"""Gets the swr_path of this ImageInfoResponse.

        **参数解释：** 镜像地址，source不同取值时，地址为不同值。 **取值范围：** 不涉及。

        :return: The swr_path of this ImageInfoResponse.
        :rtype: str
        """
        return self._swr_path

    @swr_path.setter
    def swr_path(self, swr_path):
        r"""Sets the swr_path of this ImageInfoResponse.

        **参数解释：** 镜像地址，source不同取值时，地址为不同值。 **取值范围：** 不涉及。

        :param swr_path: The swr_path of this ImageInfoResponse.
        :type swr_path: str
        """
        self._swr_path = swr_path

    @property
    def category(self):
        r"""Gets the category of this ImageInfoResponse.

        **参数解释：** 镜像支持的规格。 **取值范围：** - GPU：图形处理器。 - CPU：中央处理器。 - ASCEND：昇腾芯片。

        :return: The category of this ImageInfoResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ImageInfoResponse.

        **参数解释：** 镜像支持的规格。 **取值范围：** - GPU：图形处理器。 - CPU：中央处理器。 - ASCEND：昇腾芯片。

        :param category: The category of this ImageInfoResponse.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ImageInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
