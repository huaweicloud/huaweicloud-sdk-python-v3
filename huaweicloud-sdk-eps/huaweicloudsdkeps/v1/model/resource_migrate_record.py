# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceMigrateRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'associated': 'bool',
        'code': 'str',
        'message': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'region_id': 'str',
        'event_time': 'str',
        'user_name': 'str',
        'operate_type': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'initiate_ep_id': 'str',
        'initiate_ep_name': 'str',
        'origin_ep_id': 'str',
        'origin_ep_name': 'str',
        'target_ep_id': 'str',
        'target_ep_name': 'str',
        'exist_failed': 'str'
    }

    attribute_map = {
        'associated': 'associated',
        'code': 'code',
        'message': 'message',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'region_id': 'region_id',
        'event_time': 'event_time',
        'user_name': 'user_name',
        'operate_type': 'operate_type',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'initiate_ep_id': 'initiate_ep_id',
        'initiate_ep_name': 'initiate_ep_name',
        'origin_ep_id': 'origin_ep_id',
        'origin_ep_name': 'origin_ep_name',
        'target_ep_id': 'target_ep_id',
        'target_ep_name': 'target_ep_name',
        'exist_failed': 'exist_failed'
    }

    def __init__(self, associated=None, code=None, message=None, project_id=None, project_name=None, region_id=None, event_time=None, user_name=None, operate_type=None, resource_id=None, resource_name=None, resource_type=None, initiate_ep_id=None, initiate_ep_name=None, origin_ep_id=None, origin_ep_name=None, target_ep_id=None, target_ep_name=None, exist_failed=None):
        r"""ResourceMigrateRecord

        The model defined in huaweicloud sdk

        :param associated: 是否关联迁移
        :type associated: bool
        :param code: 响应码
        :type code: str
        :param message: 响应信息
        :type message: str
        :param project_id: 项目ID
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param region_id: 区域ID
        :type region_id: str
        :param event_time: 事件时间
        :type event_time: str
        :param user_name: 用户名
        :type user_name: str
        :param operate_type: 迁移类型
        :type operate_type: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param initiate_ep_id: 发起迁移的企业项目ID
        :type initiate_ep_id: str
        :param initiate_ep_name: 发起迁移的业项目名称
        :type initiate_ep_name: str
        :param origin_ep_id: 源企业项目ID
        :type origin_ep_id: str
        :param origin_ep_name: 源企业项目名称
        :type origin_ep_name: str
        :param target_ep_id: 目标企业项目ID
        :type target_ep_id: str
        :param target_ep_name: 目标企业项目名称
        :type target_ep_name: str
        :param exist_failed: 是否存在失败
        :type exist_failed: str
        """
        
        

        self._associated = None
        self._code = None
        self._message = None
        self._project_id = None
        self._project_name = None
        self._region_id = None
        self._event_time = None
        self._user_name = None
        self._operate_type = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._initiate_ep_id = None
        self._initiate_ep_name = None
        self._origin_ep_id = None
        self._origin_ep_name = None
        self._target_ep_id = None
        self._target_ep_name = None
        self._exist_failed = None
        self.discriminator = None

        if associated is not None:
            self.associated = associated
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if event_time is not None:
            self.event_time = event_time
        if user_name is not None:
            self.user_name = user_name
        if operate_type is not None:
            self.operate_type = operate_type
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if initiate_ep_id is not None:
            self.initiate_ep_id = initiate_ep_id
        if initiate_ep_name is not None:
            self.initiate_ep_name = initiate_ep_name
        if origin_ep_id is not None:
            self.origin_ep_id = origin_ep_id
        if origin_ep_name is not None:
            self.origin_ep_name = origin_ep_name
        if target_ep_id is not None:
            self.target_ep_id = target_ep_id
        if target_ep_name is not None:
            self.target_ep_name = target_ep_name
        if exist_failed is not None:
            self.exist_failed = exist_failed

    @property
    def associated(self):
        r"""Gets the associated of this ResourceMigrateRecord.

        是否关联迁移

        :return: The associated of this ResourceMigrateRecord.
        :rtype: bool
        """
        return self._associated

    @associated.setter
    def associated(self, associated):
        r"""Sets the associated of this ResourceMigrateRecord.

        是否关联迁移

        :param associated: The associated of this ResourceMigrateRecord.
        :type associated: bool
        """
        self._associated = associated

    @property
    def code(self):
        r"""Gets the code of this ResourceMigrateRecord.

        响应码

        :return: The code of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ResourceMigrateRecord.

        响应码

        :param code: The code of this ResourceMigrateRecord.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ResourceMigrateRecord.

        响应信息

        :return: The message of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ResourceMigrateRecord.

        响应信息

        :param message: The message of this ResourceMigrateRecord.
        :type message: str
        """
        self._message = message

    @property
    def project_id(self):
        r"""Gets the project_id of this ResourceMigrateRecord.

        项目ID

        :return: The project_id of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ResourceMigrateRecord.

        项目ID

        :param project_id: The project_id of this ResourceMigrateRecord.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this ResourceMigrateRecord.

        项目名称

        :return: The project_name of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ResourceMigrateRecord.

        项目名称

        :param project_name: The project_name of this ResourceMigrateRecord.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceMigrateRecord.

        区域ID

        :return: The region_id of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceMigrateRecord.

        区域ID

        :param region_id: The region_id of this ResourceMigrateRecord.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def event_time(self):
        r"""Gets the event_time of this ResourceMigrateRecord.

        事件时间

        :return: The event_time of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        r"""Sets the event_time of this ResourceMigrateRecord.

        事件时间

        :param event_time: The event_time of this ResourceMigrateRecord.
        :type event_time: str
        """
        self._event_time = event_time

    @property
    def user_name(self):
        r"""Gets the user_name of this ResourceMigrateRecord.

        用户名

        :return: The user_name of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ResourceMigrateRecord.

        用户名

        :param user_name: The user_name of this ResourceMigrateRecord.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def operate_type(self):
        r"""Gets the operate_type of this ResourceMigrateRecord.

        迁移类型

        :return: The operate_type of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this ResourceMigrateRecord.

        迁移类型

        :param operate_type: The operate_type of this ResourceMigrateRecord.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceMigrateRecord.

        资源ID

        :return: The resource_id of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceMigrateRecord.

        资源ID

        :param resource_id: The resource_id of this ResourceMigrateRecord.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ResourceMigrateRecord.

        资源名称

        :return: The resource_name of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ResourceMigrateRecord.

        资源名称

        :param resource_name: The resource_name of this ResourceMigrateRecord.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceMigrateRecord.

        资源类型

        :return: The resource_type of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceMigrateRecord.

        资源类型

        :param resource_type: The resource_type of this ResourceMigrateRecord.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def initiate_ep_id(self):
        r"""Gets the initiate_ep_id of this ResourceMigrateRecord.

        发起迁移的企业项目ID

        :return: The initiate_ep_id of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._initiate_ep_id

    @initiate_ep_id.setter
    def initiate_ep_id(self, initiate_ep_id):
        r"""Sets the initiate_ep_id of this ResourceMigrateRecord.

        发起迁移的企业项目ID

        :param initiate_ep_id: The initiate_ep_id of this ResourceMigrateRecord.
        :type initiate_ep_id: str
        """
        self._initiate_ep_id = initiate_ep_id

    @property
    def initiate_ep_name(self):
        r"""Gets the initiate_ep_name of this ResourceMigrateRecord.

        发起迁移的业项目名称

        :return: The initiate_ep_name of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._initiate_ep_name

    @initiate_ep_name.setter
    def initiate_ep_name(self, initiate_ep_name):
        r"""Sets the initiate_ep_name of this ResourceMigrateRecord.

        发起迁移的业项目名称

        :param initiate_ep_name: The initiate_ep_name of this ResourceMigrateRecord.
        :type initiate_ep_name: str
        """
        self._initiate_ep_name = initiate_ep_name

    @property
    def origin_ep_id(self):
        r"""Gets the origin_ep_id of this ResourceMigrateRecord.

        源企业项目ID

        :return: The origin_ep_id of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._origin_ep_id

    @origin_ep_id.setter
    def origin_ep_id(self, origin_ep_id):
        r"""Sets the origin_ep_id of this ResourceMigrateRecord.

        源企业项目ID

        :param origin_ep_id: The origin_ep_id of this ResourceMigrateRecord.
        :type origin_ep_id: str
        """
        self._origin_ep_id = origin_ep_id

    @property
    def origin_ep_name(self):
        r"""Gets the origin_ep_name of this ResourceMigrateRecord.

        源企业项目名称

        :return: The origin_ep_name of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._origin_ep_name

    @origin_ep_name.setter
    def origin_ep_name(self, origin_ep_name):
        r"""Sets the origin_ep_name of this ResourceMigrateRecord.

        源企业项目名称

        :param origin_ep_name: The origin_ep_name of this ResourceMigrateRecord.
        :type origin_ep_name: str
        """
        self._origin_ep_name = origin_ep_name

    @property
    def target_ep_id(self):
        r"""Gets the target_ep_id of this ResourceMigrateRecord.

        目标企业项目ID

        :return: The target_ep_id of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._target_ep_id

    @target_ep_id.setter
    def target_ep_id(self, target_ep_id):
        r"""Sets the target_ep_id of this ResourceMigrateRecord.

        目标企业项目ID

        :param target_ep_id: The target_ep_id of this ResourceMigrateRecord.
        :type target_ep_id: str
        """
        self._target_ep_id = target_ep_id

    @property
    def target_ep_name(self):
        r"""Gets the target_ep_name of this ResourceMigrateRecord.

        目标企业项目名称

        :return: The target_ep_name of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._target_ep_name

    @target_ep_name.setter
    def target_ep_name(self, target_ep_name):
        r"""Sets the target_ep_name of this ResourceMigrateRecord.

        目标企业项目名称

        :param target_ep_name: The target_ep_name of this ResourceMigrateRecord.
        :type target_ep_name: str
        """
        self._target_ep_name = target_ep_name

    @property
    def exist_failed(self):
        r"""Gets the exist_failed of this ResourceMigrateRecord.

        是否存在失败

        :return: The exist_failed of this ResourceMigrateRecord.
        :rtype: str
        """
        return self._exist_failed

    @exist_failed.setter
    def exist_failed(self, exist_failed):
        r"""Sets the exist_failed of this ResourceMigrateRecord.

        是否存在失败

        :param exist_failed: The exist_failed of this ResourceMigrateRecord.
        :type exist_failed: str
        """
        self._exist_failed = exist_failed

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
        if not isinstance(other, ResourceMigrateRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
