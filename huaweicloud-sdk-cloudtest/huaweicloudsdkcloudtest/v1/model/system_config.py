# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SystemConfig:

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
        'key': 'str',
        'value': 'str',
        'remark': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'update_time': 'str',
        'update_name': 'str',
        'update_num': 'str'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'value': 'value',
        'remark': 'remark',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'update_time': 'update_time',
        'update_name': 'update_name',
        'update_num': 'update_num'
    }

    def __init__(self, id=None, key=None, value=None, remark=None, region_id=None, project_id=None, update_time=None, update_name=None, update_num=None):
        r"""SystemConfig

        The model defined in huaweicloud sdk

        :param id: 配置项主键
        :type id: str
        :param key: 系统配置名称
        :type key: str
        :param value: 系统配置状态
        :type value: str
        :param remark: 描述
        :type remark: str
        :param region_id: region_id
        :type region_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param update_time: 更新时间
        :type update_time: str
        :param update_name: 更新人名称
        :type update_name: str
        :param update_num: 更新人编号
        :type update_num: str
        """
        
        

        self._id = None
        self._key = None
        self._value = None
        self._remark = None
        self._region_id = None
        self._project_id = None
        self._update_time = None
        self._update_name = None
        self._update_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if remark is not None:
            self.remark = remark
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if update_time is not None:
            self.update_time = update_time
        if update_name is not None:
            self.update_name = update_name
        if update_num is not None:
            self.update_num = update_num

    @property
    def id(self):
        r"""Gets the id of this SystemConfig.

        配置项主键

        :return: The id of this SystemConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SystemConfig.

        配置项主键

        :param id: The id of this SystemConfig.
        :type id: str
        """
        self._id = id

    @property
    def key(self):
        r"""Gets the key of this SystemConfig.

        系统配置名称

        :return: The key of this SystemConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SystemConfig.

        系统配置名称

        :param key: The key of this SystemConfig.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this SystemConfig.

        系统配置状态

        :return: The value of this SystemConfig.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this SystemConfig.

        系统配置状态

        :param value: The value of this SystemConfig.
        :type value: str
        """
        self._value = value

    @property
    def remark(self):
        r"""Gets the remark of this SystemConfig.

        描述

        :return: The remark of this SystemConfig.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this SystemConfig.

        描述

        :param remark: The remark of this SystemConfig.
        :type remark: str
        """
        self._remark = remark

    @property
    def region_id(self):
        r"""Gets the region_id of this SystemConfig.

        region_id

        :return: The region_id of this SystemConfig.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this SystemConfig.

        region_id

        :param region_id: The region_id of this SystemConfig.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this SystemConfig.

        项目ID

        :return: The project_id of this SystemConfig.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SystemConfig.

        项目ID

        :param project_id: The project_id of this SystemConfig.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def update_time(self):
        r"""Gets the update_time of this SystemConfig.

        更新时间

        :return: The update_time of this SystemConfig.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SystemConfig.

        更新时间

        :param update_time: The update_time of this SystemConfig.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_name(self):
        r"""Gets the update_name of this SystemConfig.

        更新人名称

        :return: The update_name of this SystemConfig.
        :rtype: str
        """
        return self._update_name

    @update_name.setter
    def update_name(self, update_name):
        r"""Sets the update_name of this SystemConfig.

        更新人名称

        :param update_name: The update_name of this SystemConfig.
        :type update_name: str
        """
        self._update_name = update_name

    @property
    def update_num(self):
        r"""Gets the update_num of this SystemConfig.

        更新人编号

        :return: The update_num of this SystemConfig.
        :rtype: str
        """
        return self._update_num

    @update_num.setter
    def update_num(self, update_num):
        r"""Sets the update_num of this SystemConfig.

        更新人编号

        :param update_num: The update_num of this SystemConfig.
        :type update_num: str
        """
        self._update_num = update_num

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
        if not isinstance(other, SystemConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
