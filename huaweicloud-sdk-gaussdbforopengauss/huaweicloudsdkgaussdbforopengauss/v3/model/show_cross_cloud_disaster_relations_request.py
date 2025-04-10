# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCrossCloudDisasterRelationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'limit': 'int',
        'offset': 'int',
        'instance_name': 'str',
        'instance_id': 'str',
        'dr_role': 'str',
        'dr_type': 'str',
        'dr_status': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'limit': 'limit',
        'offset': 'offset',
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'dr_role': 'dr_role',
        'dr_type': 'dr_type',
        'dr_status': 'dr_status'
    }

    def __init__(self, x_language=None, limit=None, offset=None, instance_name=None, instance_id=None, dr_role=None, dr_type=None, dr_status=None):
        r"""ShowCrossCloudDisasterRelationsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param instance_name: 实例名称，可查询过滤本端实例名称。
        :type instance_name: str
        :param instance_id: 实例id，可查询过滤本端实例id。
        :type instance_id: str
        :param dr_role: 容灾角色 - master 主 - disaster 备
        :type dr_role: str
        :param dr_type: 容灾类型 - stream - dorado
        :type dr_type: str
        :param dr_status: 状态 - normal - failover - pending - pre_check_failed - pre_checking
        :type dr_status: str
        """
        
        

        self._x_language = None
        self._limit = None
        self._offset = None
        self._instance_name = None
        self._instance_id = None
        self._dr_role = None
        self._dr_type = None
        self._dr_status = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if dr_role is not None:
            self.dr_role = dr_role
        if dr_type is not None:
            self.dr_type = dr_type
        if dr_status is not None:
            self.dr_status = dr_status

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowCrossCloudDisasterRelationsRequest.

        语言。

        :return: The x_language of this ShowCrossCloudDisasterRelationsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowCrossCloudDisasterRelationsRequest.

        语言。

        :param x_language: The x_language of this ShowCrossCloudDisasterRelationsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def limit(self):
        r"""Gets the limit of this ShowCrossCloudDisasterRelationsRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ShowCrossCloudDisasterRelationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowCrossCloudDisasterRelationsRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ShowCrossCloudDisasterRelationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowCrossCloudDisasterRelationsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ShowCrossCloudDisasterRelationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowCrossCloudDisasterRelationsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ShowCrossCloudDisasterRelationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowCrossCloudDisasterRelationsRequest.

        实例名称，可查询过滤本端实例名称。

        :return: The instance_name of this ShowCrossCloudDisasterRelationsRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowCrossCloudDisasterRelationsRequest.

        实例名称，可查询过滤本端实例名称。

        :param instance_name: The instance_name of this ShowCrossCloudDisasterRelationsRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowCrossCloudDisasterRelationsRequest.

        实例id，可查询过滤本端实例id。

        :return: The instance_id of this ShowCrossCloudDisasterRelationsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowCrossCloudDisasterRelationsRequest.

        实例id，可查询过滤本端实例id。

        :param instance_id: The instance_id of this ShowCrossCloudDisasterRelationsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def dr_role(self):
        r"""Gets the dr_role of this ShowCrossCloudDisasterRelationsRequest.

        容灾角色 - master 主 - disaster 备

        :return: The dr_role of this ShowCrossCloudDisasterRelationsRequest.
        :rtype: str
        """
        return self._dr_role

    @dr_role.setter
    def dr_role(self, dr_role):
        r"""Sets the dr_role of this ShowCrossCloudDisasterRelationsRequest.

        容灾角色 - master 主 - disaster 备

        :param dr_role: The dr_role of this ShowCrossCloudDisasterRelationsRequest.
        :type dr_role: str
        """
        self._dr_role = dr_role

    @property
    def dr_type(self):
        r"""Gets the dr_type of this ShowCrossCloudDisasterRelationsRequest.

        容灾类型 - stream - dorado

        :return: The dr_type of this ShowCrossCloudDisasterRelationsRequest.
        :rtype: str
        """
        return self._dr_type

    @dr_type.setter
    def dr_type(self, dr_type):
        r"""Sets the dr_type of this ShowCrossCloudDisasterRelationsRequest.

        容灾类型 - stream - dorado

        :param dr_type: The dr_type of this ShowCrossCloudDisasterRelationsRequest.
        :type dr_type: str
        """
        self._dr_type = dr_type

    @property
    def dr_status(self):
        r"""Gets the dr_status of this ShowCrossCloudDisasterRelationsRequest.

        状态 - normal - failover - pending - pre_check_failed - pre_checking

        :return: The dr_status of this ShowCrossCloudDisasterRelationsRequest.
        :rtype: str
        """
        return self._dr_status

    @dr_status.setter
    def dr_status(self, dr_status):
        r"""Sets the dr_status of this ShowCrossCloudDisasterRelationsRequest.

        状态 - normal - failover - pending - pre_check_failed - pre_checking

        :param dr_status: The dr_status of this ShowCrossCloudDisasterRelationsRequest.
        :type dr_status: str
        """
        self._dr_status = dr_status

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
        if not isinstance(other, ShowCrossCloudDisasterRelationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
