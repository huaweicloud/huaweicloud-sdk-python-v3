# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertTemplateVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_levels': 'list[AlertLevel]',
        'create_time': 'str',
        'create_user': 'str',
        'id': 'str',
        'name': 'str',
        'remarks': 'str',
        'test_service_id': 'str',
        'update_time': 'str',
        'update_user': 'str'
    }

    attribute_map = {
        'alert_levels': 'alertLevels',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'id': 'id',
        'name': 'name',
        'remarks': 'remarks',
        'test_service_id': 'test_service_id',
        'update_time': 'update_time',
        'update_user': 'update_user'
    }

    def __init__(self, alert_levels=None, create_time=None, create_user=None, id=None, name=None, remarks=None, test_service_id=None, update_time=None, update_user=None):
        """AlertTemplateVo

        The model defined in huaweicloud sdk

        :param alert_levels: 告警级别列表
        :type alert_levels: list[:class:`huaweicloudsdkcloudtest.v1.AlertLevel`]
        :param create_time: 创建时间
        :type create_time: str
        :param create_user: 创建人
        :type create_user: str
        :param id: 唯一ID，主键
        :type id: str
        :param name: 告警模板名称
        :type name: str
        :param remarks: 备注
        :type remarks: str
        :param test_service_id: 服务ID
        :type test_service_id: str
        :param update_time: 创建时间
        :type update_time: str
        :param update_user: 更新人
        :type update_user: str
        """
        
        

        self._alert_levels = None
        self._create_time = None
        self._create_user = None
        self._id = None
        self._name = None
        self._remarks = None
        self._test_service_id = None
        self._update_time = None
        self._update_user = None
        self.discriminator = None

        if alert_levels is not None:
            self.alert_levels = alert_levels
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if remarks is not None:
            self.remarks = remarks
        if test_service_id is not None:
            self.test_service_id = test_service_id
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user

    @property
    def alert_levels(self):
        """Gets the alert_levels of this AlertTemplateVo.

        告警级别列表

        :return: The alert_levels of this AlertTemplateVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AlertLevel`]
        """
        return self._alert_levels

    @alert_levels.setter
    def alert_levels(self, alert_levels):
        """Sets the alert_levels of this AlertTemplateVo.

        告警级别列表

        :param alert_levels: The alert_levels of this AlertTemplateVo.
        :type alert_levels: list[:class:`huaweicloudsdkcloudtest.v1.AlertLevel`]
        """
        self._alert_levels = alert_levels

    @property
    def create_time(self):
        """Gets the create_time of this AlertTemplateVo.

        创建时间

        :return: The create_time of this AlertTemplateVo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AlertTemplateVo.

        创建时间

        :param create_time: The create_time of this AlertTemplateVo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this AlertTemplateVo.

        创建人

        :return: The create_user of this AlertTemplateVo.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this AlertTemplateVo.

        创建人

        :param create_user: The create_user of this AlertTemplateVo.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def id(self):
        """Gets the id of this AlertTemplateVo.

        唯一ID，主键

        :return: The id of this AlertTemplateVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertTemplateVo.

        唯一ID，主键

        :param id: The id of this AlertTemplateVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AlertTemplateVo.

        告警模板名称

        :return: The name of this AlertTemplateVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertTemplateVo.

        告警模板名称

        :param name: The name of this AlertTemplateVo.
        :type name: str
        """
        self._name = name

    @property
    def remarks(self):
        """Gets the remarks of this AlertTemplateVo.

        备注

        :return: The remarks of this AlertTemplateVo.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this AlertTemplateVo.

        备注

        :param remarks: The remarks of this AlertTemplateVo.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def test_service_id(self):
        """Gets the test_service_id of this AlertTemplateVo.

        服务ID

        :return: The test_service_id of this AlertTemplateVo.
        :rtype: str
        """
        return self._test_service_id

    @test_service_id.setter
    def test_service_id(self, test_service_id):
        """Sets the test_service_id of this AlertTemplateVo.

        服务ID

        :param test_service_id: The test_service_id of this AlertTemplateVo.
        :type test_service_id: str
        """
        self._test_service_id = test_service_id

    @property
    def update_time(self):
        """Gets the update_time of this AlertTemplateVo.

        创建时间

        :return: The update_time of this AlertTemplateVo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AlertTemplateVo.

        创建时间

        :param update_time: The update_time of this AlertTemplateVo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_user(self):
        """Gets the update_user of this AlertTemplateVo.

        更新人

        :return: The update_user of this AlertTemplateVo.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this AlertTemplateVo.

        更新人

        :param update_user: The update_user of this AlertTemplateVo.
        :type update_user: str
        """
        self._update_user = update_user

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
        if not isinstance(other, AlertTemplateVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
