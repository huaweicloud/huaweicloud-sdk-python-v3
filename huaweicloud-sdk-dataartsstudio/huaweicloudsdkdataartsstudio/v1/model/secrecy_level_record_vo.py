# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecrecyLevelRecordVO:

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
        'secrecy_level_id': 'str',
        'secrecy_level_name': 'str',
        'uuid': 'str',
        'slevel': 'int',
        'description': 'str',
        'biz_id': 'str',
        'biz_type': 'BizTypeEnum',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'secrecy_level_id': 'secrecyLevel_id',
        'secrecy_level_name': 'secrecyLevel_name',
        'uuid': 'uuid',
        'slevel': 'slevel',
        'description': 'description',
        'biz_id': 'biz_id',
        'biz_type': 'biz_type',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, secrecy_level_id=None, secrecy_level_name=None, uuid=None, slevel=None, description=None, biz_id=None, biz_type=None, create_by=None, update_by=None, create_time=None, update_time=None):
        r"""SecrecyLevelRecordVO

        The model defined in huaweicloud sdk

        :param id: 属性关联密级的ID，ID字符串。
        :type id: str
        :param secrecy_level_id: 密级的ID，ID字符串。
        :type secrecy_level_id: str
        :param secrecy_level_name: 密级名称。
        :type secrecy_level_name: str
        :param uuid: 数据安全主键。
        :type uuid: str
        :param slevel: 密级等级。
        :type slevel: int
        :param description: 密级描述。
        :type description: str
        :param biz_id: 业务对象ID，ID字符串。
        :type biz_id: str
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param create_by: 创建者。
        :type create_by: str
        :param update_by: 更新者。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._secrecy_level_id = None
        self._secrecy_level_name = None
        self._uuid = None
        self._slevel = None
        self._description = None
        self._biz_id = None
        self._biz_type = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.secrecy_level_id = secrecy_level_id
        if secrecy_level_name is not None:
            self.secrecy_level_name = secrecy_level_name
        if uuid is not None:
            self.uuid = uuid
        if slevel is not None:
            self.slevel = slevel
        if description is not None:
            self.description = description
        self.biz_id = biz_id
        self.biz_type = biz_type
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this SecrecyLevelRecordVO.

        属性关联密级的ID，ID字符串。

        :return: The id of this SecrecyLevelRecordVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SecrecyLevelRecordVO.

        属性关联密级的ID，ID字符串。

        :param id: The id of this SecrecyLevelRecordVO.
        :type id: str
        """
        self._id = id

    @property
    def secrecy_level_id(self):
        r"""Gets the secrecy_level_id of this SecrecyLevelRecordVO.

        密级的ID，ID字符串。

        :return: The secrecy_level_id of this SecrecyLevelRecordVO.
        :rtype: str
        """
        return self._secrecy_level_id

    @secrecy_level_id.setter
    def secrecy_level_id(self, secrecy_level_id):
        r"""Sets the secrecy_level_id of this SecrecyLevelRecordVO.

        密级的ID，ID字符串。

        :param secrecy_level_id: The secrecy_level_id of this SecrecyLevelRecordVO.
        :type secrecy_level_id: str
        """
        self._secrecy_level_id = secrecy_level_id

    @property
    def secrecy_level_name(self):
        r"""Gets the secrecy_level_name of this SecrecyLevelRecordVO.

        密级名称。

        :return: The secrecy_level_name of this SecrecyLevelRecordVO.
        :rtype: str
        """
        return self._secrecy_level_name

    @secrecy_level_name.setter
    def secrecy_level_name(self, secrecy_level_name):
        r"""Sets the secrecy_level_name of this SecrecyLevelRecordVO.

        密级名称。

        :param secrecy_level_name: The secrecy_level_name of this SecrecyLevelRecordVO.
        :type secrecy_level_name: str
        """
        self._secrecy_level_name = secrecy_level_name

    @property
    def uuid(self):
        r"""Gets the uuid of this SecrecyLevelRecordVO.

        数据安全主键。

        :return: The uuid of this SecrecyLevelRecordVO.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this SecrecyLevelRecordVO.

        数据安全主键。

        :param uuid: The uuid of this SecrecyLevelRecordVO.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def slevel(self):
        r"""Gets the slevel of this SecrecyLevelRecordVO.

        密级等级。

        :return: The slevel of this SecrecyLevelRecordVO.
        :rtype: int
        """
        return self._slevel

    @slevel.setter
    def slevel(self, slevel):
        r"""Sets the slevel of this SecrecyLevelRecordVO.

        密级等级。

        :param slevel: The slevel of this SecrecyLevelRecordVO.
        :type slevel: int
        """
        self._slevel = slevel

    @property
    def description(self):
        r"""Gets the description of this SecrecyLevelRecordVO.

        密级描述。

        :return: The description of this SecrecyLevelRecordVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SecrecyLevelRecordVO.

        密级描述。

        :param description: The description of this SecrecyLevelRecordVO.
        :type description: str
        """
        self._description = description

    @property
    def biz_id(self):
        r"""Gets the biz_id of this SecrecyLevelRecordVO.

        业务对象ID，ID字符串。

        :return: The biz_id of this SecrecyLevelRecordVO.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this SecrecyLevelRecordVO.

        业务对象ID，ID字符串。

        :param biz_id: The biz_id of this SecrecyLevelRecordVO.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def biz_type(self):
        r"""Gets the biz_type of this SecrecyLevelRecordVO.

        :return: The biz_type of this SecrecyLevelRecordVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this SecrecyLevelRecordVO.

        :param biz_type: The biz_type of this SecrecyLevelRecordVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def create_by(self):
        r"""Gets the create_by of this SecrecyLevelRecordVO.

        创建者。

        :return: The create_by of this SecrecyLevelRecordVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this SecrecyLevelRecordVO.

        创建者。

        :param create_by: The create_by of this SecrecyLevelRecordVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this SecrecyLevelRecordVO.

        更新者。

        :return: The update_by of this SecrecyLevelRecordVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this SecrecyLevelRecordVO.

        更新者。

        :param update_by: The update_by of this SecrecyLevelRecordVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        r"""Gets the create_time of this SecrecyLevelRecordVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this SecrecyLevelRecordVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SecrecyLevelRecordVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this SecrecyLevelRecordVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this SecrecyLevelRecordVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this SecrecyLevelRecordVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SecrecyLevelRecordVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this SecrecyLevelRecordVO.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, SecrecyLevelRecordVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
