# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchChangeServerImageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_ids': 'list[str]',
        'image_id': 'str',
        'image_type': 'ImageTypeEnum',
        'os_type': 'OsTypeEnum',
        'image_product_id': 'str',
        'update_access_agent': 'bool'
    }

    attribute_map = {
        'server_ids': 'server_ids',
        'image_id': 'image_id',
        'image_type': 'image_type',
        'os_type': 'os_type',
        'image_product_id': 'image_product_id',
        'update_access_agent': 'update_access_agent'
    }

    def __init__(self, server_ids=None, image_id=None, image_type=None, os_type=None, image_product_id=None, update_access_agent=None):
        r"""BatchChangeServerImageReq

        The model defined in huaweicloud sdk

        :param server_ids: 应用服务器id集合。
        :type server_ids: list[str]
        :param image_id: 镜像id，要求与服务器原有镜像id不相同。
        :type image_id: str
        :param image_type: 
        :type image_type: :class:`huaweicloudsdkworkspaceapp.v1.ImageTypeEnum`
        :param os_type: 
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        :param image_product_id: 镜像的产品id，当镜像是市场镜像时候，该字段必传。
        :type image_product_id: str
        :param update_access_agent: 是否自动升级hda版本。
        :type update_access_agent: bool
        """
        
        

        self._server_ids = None
        self._image_id = None
        self._image_type = None
        self._os_type = None
        self._image_product_id = None
        self._update_access_agent = None
        self.discriminator = None

        if server_ids is not None:
            self.server_ids = server_ids
        self.image_id = image_id
        self.image_type = image_type
        self.os_type = os_type
        if image_product_id is not None:
            self.image_product_id = image_product_id
        if update_access_agent is not None:
            self.update_access_agent = update_access_agent

    @property
    def server_ids(self):
        r"""Gets the server_ids of this BatchChangeServerImageReq.

        应用服务器id集合。

        :return: The server_ids of this BatchChangeServerImageReq.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        r"""Sets the server_ids of this BatchChangeServerImageReq.

        应用服务器id集合。

        :param server_ids: The server_ids of this BatchChangeServerImageReq.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def image_id(self):
        r"""Gets the image_id of this BatchChangeServerImageReq.

        镜像id，要求与服务器原有镜像id不相同。

        :return: The image_id of this BatchChangeServerImageReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this BatchChangeServerImageReq.

        镜像id，要求与服务器原有镜像id不相同。

        :param image_id: The image_id of this BatchChangeServerImageReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_type(self):
        r"""Gets the image_type of this BatchChangeServerImageReq.

        :return: The image_type of this BatchChangeServerImageReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ImageTypeEnum`
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this BatchChangeServerImageReq.

        :param image_type: The image_type of this BatchChangeServerImageReq.
        :type image_type: :class:`huaweicloudsdkworkspaceapp.v1.ImageTypeEnum`
        """
        self._image_type = image_type

    @property
    def os_type(self):
        r"""Gets the os_type of this BatchChangeServerImageReq.

        :return: The os_type of this BatchChangeServerImageReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this BatchChangeServerImageReq.

        :param os_type: The os_type of this BatchChangeServerImageReq.
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        self._os_type = os_type

    @property
    def image_product_id(self):
        r"""Gets the image_product_id of this BatchChangeServerImageReq.

        镜像的产品id，当镜像是市场镜像时候，该字段必传。

        :return: The image_product_id of this BatchChangeServerImageReq.
        :rtype: str
        """
        return self._image_product_id

    @image_product_id.setter
    def image_product_id(self, image_product_id):
        r"""Sets the image_product_id of this BatchChangeServerImageReq.

        镜像的产品id，当镜像是市场镜像时候，该字段必传。

        :param image_product_id: The image_product_id of this BatchChangeServerImageReq.
        :type image_product_id: str
        """
        self._image_product_id = image_product_id

    @property
    def update_access_agent(self):
        r"""Gets the update_access_agent of this BatchChangeServerImageReq.

        是否自动升级hda版本。

        :return: The update_access_agent of this BatchChangeServerImageReq.
        :rtype: bool
        """
        return self._update_access_agent

    @update_access_agent.setter
    def update_access_agent(self, update_access_agent):
        r"""Sets the update_access_agent of this BatchChangeServerImageReq.

        是否自动升级hda版本。

        :param update_access_agent: The update_access_agent of this BatchChangeServerImageReq.
        :type update_access_agent: bool
        """
        self._update_access_agent = update_access_agent

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
        if not isinstance(other, BatchChangeServerImageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
