# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableZoneV2:

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
        'az_code': 'str',
        'az_name': 'str',
        'az_id': 'str',
        'status': 'str',
        'region_id': 'str',
        'az_group_id': 'str',
        'az_type': 'str',
        'az_tags': 'AvailableTag'
    }

    attribute_map = {
        'id': 'id',
        'az_code': 'az_code',
        'az_name': 'az_name',
        'az_id': 'az_id',
        'status': 'status',
        'region_id': 'region_id',
        'az_group_id': 'az_group_id',
        'az_type': 'az_type',
        'az_tags': 'az_tags'
    }

    def __init__(self, id=None, az_code=None, az_name=None, az_id=None, status=None, region_id=None, az_group_id=None, az_type=None, az_tags=None):
        """AvailableZoneV2

        The model defined in huaweicloud sdk

        :param id: 可用区编码
        :type id: str
        :param az_code: 可用区编码
        :type az_code: str
        :param az_name: 可用区名称
        :type az_name: str
        :param az_id: 可用区id
        :type az_id: str
        :param status: 可用区状态
        :type status: str
        :param region_id: 区域id
        :type region_id: str
        :param az_group_id: 可用区分组id
        :type az_group_id: str
        :param az_type: 当前AZ的类型 Core 核心 Satellite 卫星 Dedicated 专属 Virtual 虚拟 Edge 边缘 EdgeCental 中心边缘 Hybrid 混合云
        :type az_type: str
        :param az_tags: 
        :type az_tags: :class:`huaweicloudsdkmrs.v1.AvailableTag`
        """
        
        

        self._id = None
        self._az_code = None
        self._az_name = None
        self._az_id = None
        self._status = None
        self._region_id = None
        self._az_group_id = None
        self._az_type = None
        self._az_tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if az_code is not None:
            self.az_code = az_code
        if az_name is not None:
            self.az_name = az_name
        if az_id is not None:
            self.az_id = az_id
        if status is not None:
            self.status = status
        if region_id is not None:
            self.region_id = region_id
        if az_group_id is not None:
            self.az_group_id = az_group_id
        if az_type is not None:
            self.az_type = az_type
        if az_tags is not None:
            self.az_tags = az_tags

    @property
    def id(self):
        """Gets the id of this AvailableZoneV2.

        可用区编码

        :return: The id of this AvailableZoneV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AvailableZoneV2.

        可用区编码

        :param id: The id of this AvailableZoneV2.
        :type id: str
        """
        self._id = id

    @property
    def az_code(self):
        """Gets the az_code of this AvailableZoneV2.

        可用区编码

        :return: The az_code of this AvailableZoneV2.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this AvailableZoneV2.

        可用区编码

        :param az_code: The az_code of this AvailableZoneV2.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def az_name(self):
        """Gets the az_name of this AvailableZoneV2.

        可用区名称

        :return: The az_name of this AvailableZoneV2.
        :rtype: str
        """
        return self._az_name

    @az_name.setter
    def az_name(self, az_name):
        """Sets the az_name of this AvailableZoneV2.

        可用区名称

        :param az_name: The az_name of this AvailableZoneV2.
        :type az_name: str
        """
        self._az_name = az_name

    @property
    def az_id(self):
        """Gets the az_id of this AvailableZoneV2.

        可用区id

        :return: The az_id of this AvailableZoneV2.
        :rtype: str
        """
        return self._az_id

    @az_id.setter
    def az_id(self, az_id):
        """Sets the az_id of this AvailableZoneV2.

        可用区id

        :param az_id: The az_id of this AvailableZoneV2.
        :type az_id: str
        """
        self._az_id = az_id

    @property
    def status(self):
        """Gets the status of this AvailableZoneV2.

        可用区状态

        :return: The status of this AvailableZoneV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AvailableZoneV2.

        可用区状态

        :param status: The status of this AvailableZoneV2.
        :type status: str
        """
        self._status = status

    @property
    def region_id(self):
        """Gets the region_id of this AvailableZoneV2.

        区域id

        :return: The region_id of this AvailableZoneV2.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this AvailableZoneV2.

        区域id

        :param region_id: The region_id of this AvailableZoneV2.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def az_group_id(self):
        """Gets the az_group_id of this AvailableZoneV2.

        可用区分组id

        :return: The az_group_id of this AvailableZoneV2.
        :rtype: str
        """
        return self._az_group_id

    @az_group_id.setter
    def az_group_id(self, az_group_id):
        """Sets the az_group_id of this AvailableZoneV2.

        可用区分组id

        :param az_group_id: The az_group_id of this AvailableZoneV2.
        :type az_group_id: str
        """
        self._az_group_id = az_group_id

    @property
    def az_type(self):
        """Gets the az_type of this AvailableZoneV2.

        当前AZ的类型 Core 核心 Satellite 卫星 Dedicated 专属 Virtual 虚拟 Edge 边缘 EdgeCental 中心边缘 Hybrid 混合云

        :return: The az_type of this AvailableZoneV2.
        :rtype: str
        """
        return self._az_type

    @az_type.setter
    def az_type(self, az_type):
        """Sets the az_type of this AvailableZoneV2.

        当前AZ的类型 Core 核心 Satellite 卫星 Dedicated 专属 Virtual 虚拟 Edge 边缘 EdgeCental 中心边缘 Hybrid 混合云

        :param az_type: The az_type of this AvailableZoneV2.
        :type az_type: str
        """
        self._az_type = az_type

    @property
    def az_tags(self):
        """Gets the az_tags of this AvailableZoneV2.

        :return: The az_tags of this AvailableZoneV2.
        :rtype: :class:`huaweicloudsdkmrs.v1.AvailableTag`
        """
        return self._az_tags

    @az_tags.setter
    def az_tags(self, az_tags):
        """Sets the az_tags of this AvailableZoneV2.

        :param az_tags: The az_tags of this AvailableZoneV2.
        :type az_tags: :class:`huaweicloudsdkmrs.v1.AvailableTag`
        """
        self._az_tags = az_tags

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
        if not isinstance(other, AvailableZoneV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
