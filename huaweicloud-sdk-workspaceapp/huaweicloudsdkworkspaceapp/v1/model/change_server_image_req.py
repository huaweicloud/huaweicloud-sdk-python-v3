# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeServerImageReq:

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
        'image_type': 'ImageTypeEnum',
        'os_type': 'OsTypeEnum',
        'image_product_id': 'str',
        'update_access_agent': 'bool'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_type': 'image_type',
        'os_type': 'os_type',
        'image_product_id': 'image_product_id',
        'update_access_agent': 'update_access_agent'
    }

    def __init__(self, image_id=None, image_type=None, os_type=None, image_product_id=None, update_access_agent=None):
        """ChangeServerImageReq

        The model defined in huaweicloud sdk

        :param image_id: 镜像id，要求与服务器原有镜像id不相同
        :type image_id: str
        :param image_type: 
        :type image_type: :class:`huaweicloudsdkworkspaceapp.v1.ImageTypeEnum`
        :param os_type: 
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        :param image_product_id: 镜像的产品id，当镜像是市场镜像时候，该字段必传
        :type image_product_id: str
        :param update_access_agent: 是否自动升级hda版本
        :type update_access_agent: bool
        """
        
        

        self._image_id = None
        self._image_type = None
        self._os_type = None
        self._image_product_id = None
        self._update_access_agent = None
        self.discriminator = None

        self.image_id = image_id
        self.image_type = image_type
        self.os_type = os_type
        if image_product_id is not None:
            self.image_product_id = image_product_id
        if update_access_agent is not None:
            self.update_access_agent = update_access_agent

    @property
    def image_id(self):
        """Gets the image_id of this ChangeServerImageReq.

        镜像id，要求与服务器原有镜像id不相同

        :return: The image_id of this ChangeServerImageReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ChangeServerImageReq.

        镜像id，要求与服务器原有镜像id不相同

        :param image_id: The image_id of this ChangeServerImageReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_type(self):
        """Gets the image_type of this ChangeServerImageReq.

        :return: The image_type of this ChangeServerImageReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ImageTypeEnum`
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ChangeServerImageReq.

        :param image_type: The image_type of this ChangeServerImageReq.
        :type image_type: :class:`huaweicloudsdkworkspaceapp.v1.ImageTypeEnum`
        """
        self._image_type = image_type

    @property
    def os_type(self):
        """Gets the os_type of this ChangeServerImageReq.

        :return: The os_type of this ChangeServerImageReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ChangeServerImageReq.

        :param os_type: The os_type of this ChangeServerImageReq.
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        self._os_type = os_type

    @property
    def image_product_id(self):
        """Gets the image_product_id of this ChangeServerImageReq.

        镜像的产品id，当镜像是市场镜像时候，该字段必传

        :return: The image_product_id of this ChangeServerImageReq.
        :rtype: str
        """
        return self._image_product_id

    @image_product_id.setter
    def image_product_id(self, image_product_id):
        """Sets the image_product_id of this ChangeServerImageReq.

        镜像的产品id，当镜像是市场镜像时候，该字段必传

        :param image_product_id: The image_product_id of this ChangeServerImageReq.
        :type image_product_id: str
        """
        self._image_product_id = image_product_id

    @property
    def update_access_agent(self):
        """Gets the update_access_agent of this ChangeServerImageReq.

        是否自动升级hda版本

        :return: The update_access_agent of this ChangeServerImageReq.
        :rtype: bool
        """
        return self._update_access_agent

    @update_access_agent.setter
    def update_access_agent(self, update_access_agent):
        """Sets the update_access_agent of this ChangeServerImageReq.

        是否自动升级hda版本

        :param update_access_agent: The update_access_agent of this ChangeServerImageReq.
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
        if not isinstance(other, ChangeServerImageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
