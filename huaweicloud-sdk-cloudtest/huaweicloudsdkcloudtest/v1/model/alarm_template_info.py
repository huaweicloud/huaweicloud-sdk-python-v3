# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmTemplateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'create_user': 'str',
        'id': 'str',
        'remarks': 'str',
        'test_service_id': 'str',
        'update_time': 'str',
        'update_user': 'str',
        'name': 'str'
    }

    attribute_map = {
        'create_time': 'createTime',
        'create_user': 'createUser',
        'id': 'id',
        'remarks': 'remarks',
        'test_service_id': 'testServiceId',
        'update_time': 'updateTime',
        'update_user': 'updateUser',
        'name': 'name'
    }

    def __init__(self, create_time=None, create_user=None, id=None, remarks=None, test_service_id=None, update_time=None, update_user=None, name=None):
        r"""AlarmTemplateInfo

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param create_user: 创建者
        :type create_user: str
        :param id: UUID
        :type id: str
        :param remarks: 备注
        :type remarks: str
        :param test_service_id: 服务id
        :type test_service_id: str
        :param update_time: 修改时间
        :type update_time: str
        :param update_user: 修改者
        :type update_user: str
        :param name: 模板名称
        :type name: str
        """
        
        

        self._create_time = None
        self._create_user = None
        self._id = None
        self._remarks = None
        self._test_service_id = None
        self._update_time = None
        self._update_user = None
        self._name = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if id is not None:
            self.id = id
        if remarks is not None:
            self.remarks = remarks
        if test_service_id is not None:
            self.test_service_id = test_service_id
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if name is not None:
            self.name = name

    @property
    def create_time(self):
        r"""Gets the create_time of this AlarmTemplateInfo.

        创建时间

        :return: The create_time of this AlarmTemplateInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AlarmTemplateInfo.

        创建时间

        :param create_time: The create_time of this AlarmTemplateInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this AlarmTemplateInfo.

        创建者

        :return: The create_user of this AlarmTemplateInfo.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this AlarmTemplateInfo.

        创建者

        :param create_user: The create_user of this AlarmTemplateInfo.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def id(self):
        r"""Gets the id of this AlarmTemplateInfo.

        UUID

        :return: The id of this AlarmTemplateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlarmTemplateInfo.

        UUID

        :param id: The id of this AlarmTemplateInfo.
        :type id: str
        """
        self._id = id

    @property
    def remarks(self):
        r"""Gets the remarks of this AlarmTemplateInfo.

        备注

        :return: The remarks of this AlarmTemplateInfo.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this AlarmTemplateInfo.

        备注

        :param remarks: The remarks of this AlarmTemplateInfo.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def test_service_id(self):
        r"""Gets the test_service_id of this AlarmTemplateInfo.

        服务id

        :return: The test_service_id of this AlarmTemplateInfo.
        :rtype: str
        """
        return self._test_service_id

    @test_service_id.setter
    def test_service_id(self, test_service_id):
        r"""Sets the test_service_id of this AlarmTemplateInfo.

        服务id

        :param test_service_id: The test_service_id of this AlarmTemplateInfo.
        :type test_service_id: str
        """
        self._test_service_id = test_service_id

    @property
    def update_time(self):
        r"""Gets the update_time of this AlarmTemplateInfo.

        修改时间

        :return: The update_time of this AlarmTemplateInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AlarmTemplateInfo.

        修改时间

        :param update_time: The update_time of this AlarmTemplateInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this AlarmTemplateInfo.

        修改者

        :return: The update_user of this AlarmTemplateInfo.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this AlarmTemplateInfo.

        修改者

        :param update_user: The update_user of this AlarmTemplateInfo.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def name(self):
        r"""Gets the name of this AlarmTemplateInfo.

        模板名称

        :return: The name of this AlarmTemplateInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlarmTemplateInfo.

        模板名称

        :param name: The name of this AlarmTemplateInfo.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AlarmTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
