# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQueueDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'queue_name': 'str',
        'description': 'str',
        'owner': 'str',
        'create_time': 'int',
        'cu_count': 'int',
        'charging_mode': 'int',
        'resource_id': 'str',
        'queue_type': 'str',
        'resource_type': 'str',
        'resource_mode': 'int',
        'enterprise_project_id': 'str',
        'cu_spec': 'int',
        'cu_scale_out_limit': 'int',
        'cu_scale_in_limit': 'int'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'queue_name': 'queueName',
        'description': 'description',
        'owner': 'owner',
        'create_time': 'create_time',
        'cu_count': 'cuCount',
        'charging_mode': 'chargingMode',
        'resource_id': 'resource_id',
        'queue_type': 'queueType',
        'resource_type': 'resource_type',
        'resource_mode': 'resource_mode',
        'enterprise_project_id': 'enterprise_project_id',
        'cu_spec': 'cu_spec',
        'cu_scale_out_limit': 'cu_scale_out_limit',
        'cu_scale_in_limit': 'cu_scale_in_limit'
    }

    def __init__(self, is_success=None, message=None, queue_name=None, description=None, owner=None, create_time=None, cu_count=None, charging_mode=None, resource_id=None, queue_type=None, resource_type=None, resource_mode=None, enterprise_project_id=None, cu_spec=None, cu_scale_out_limit=None, cu_scale_in_limit=None):
        """ShowQueueDetailResponse

        The model defined in huaweicloud sdk

        :param is_success: 请求执行是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param queue_name: 队列名称。
        :type queue_name: str
        :param description: 队列描述信息。
        :type description: str
        :param owner: 创建队列的用户。
        :type owner: str
        :param create_time: 创建队列的时间。是单位为“毫秒”的时间戳。
        :type create_time: int
        :param cu_count: 与队列绑定的最小计算单元个数。设置值当前只支持16，64，256。
        :type cu_count: int
        :param charging_mode: 队列的收费模式。 “1”表示按照CU时收费。 “2”表示按照包年包月收费。
        :type charging_mode: int
        :param resource_id: 队列的资源ID。
        :type resource_id: str
        :param queue_type: 队列的资源ID。
        :type queue_type: str
        :param resource_type: 队列的资源ID。
        :type resource_type: str
        :param resource_mode: 队列类型。 0：共享队列 1：专属队列
        :type resource_mode: int
        :param enterprise_project_id: 企业项目ID。\&quot;0”表示default，即默认的企业项目。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。
        :type enterprise_project_id: str
        :param cu_spec: 队列的规格大小。对于包周期队列，表示包周期部分的CU值；对于按需队列，表示用户购买队列时的初始值。
        :type cu_spec: int
        :param cu_scale_out_limit: 当前队列弹性扩缩容的CU值上限。
        :type cu_scale_out_limit: int
        :param cu_scale_in_limit: 当前队列弹性扩缩容的CU值下限。
        :type cu_scale_in_limit: int
        """
        
        super(ShowQueueDetailResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._queue_name = None
        self._description = None
        self._owner = None
        self._create_time = None
        self._cu_count = None
        self._charging_mode = None
        self._resource_id = None
        self._queue_type = None
        self._resource_type = None
        self._resource_mode = None
        self._enterprise_project_id = None
        self._cu_spec = None
        self._cu_scale_out_limit = None
        self._cu_scale_in_limit = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if queue_name is not None:
            self.queue_name = queue_name
        if description is not None:
            self.description = description
        if owner is not None:
            self.owner = owner
        if create_time is not None:
            self.create_time = create_time
        if cu_count is not None:
            self.cu_count = cu_count
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_id is not None:
            self.resource_id = resource_id
        if queue_type is not None:
            self.queue_type = queue_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_mode is not None:
            self.resource_mode = resource_mode
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if cu_spec is not None:
            self.cu_spec = cu_spec
        if cu_scale_out_limit is not None:
            self.cu_scale_out_limit = cu_scale_out_limit
        if cu_scale_in_limit is not None:
            self.cu_scale_in_limit = cu_scale_in_limit

    @property
    def is_success(self):
        """Gets the is_success of this ShowQueueDetailResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :return: The is_success of this ShowQueueDetailResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ShowQueueDetailResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ShowQueueDetailResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ShowQueueDetailResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ShowQueueDetailResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowQueueDetailResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ShowQueueDetailResponse.
        :type message: str
        """
        self._message = message

    @property
    def queue_name(self):
        """Gets the queue_name of this ShowQueueDetailResponse.

        队列名称。

        :return: The queue_name of this ShowQueueDetailResponse.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ShowQueueDetailResponse.

        队列名称。

        :param queue_name: The queue_name of this ShowQueueDetailResponse.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def description(self):
        """Gets the description of this ShowQueueDetailResponse.

        队列描述信息。

        :return: The description of this ShowQueueDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowQueueDetailResponse.

        队列描述信息。

        :param description: The description of this ShowQueueDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def owner(self):
        """Gets the owner of this ShowQueueDetailResponse.

        创建队列的用户。

        :return: The owner of this ShowQueueDetailResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowQueueDetailResponse.

        创建队列的用户。

        :param owner: The owner of this ShowQueueDetailResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def create_time(self):
        """Gets the create_time of this ShowQueueDetailResponse.

        创建队列的时间。是单位为“毫秒”的时间戳。

        :return: The create_time of this ShowQueueDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowQueueDetailResponse.

        创建队列的时间。是单位为“毫秒”的时间戳。

        :param create_time: The create_time of this ShowQueueDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def cu_count(self):
        """Gets the cu_count of this ShowQueueDetailResponse.

        与队列绑定的最小计算单元个数。设置值当前只支持16，64，256。

        :return: The cu_count of this ShowQueueDetailResponse.
        :rtype: int
        """
        return self._cu_count

    @cu_count.setter
    def cu_count(self, cu_count):
        """Sets the cu_count of this ShowQueueDetailResponse.

        与队列绑定的最小计算单元个数。设置值当前只支持16，64，256。

        :param cu_count: The cu_count of this ShowQueueDetailResponse.
        :type cu_count: int
        """
        self._cu_count = cu_count

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ShowQueueDetailResponse.

        队列的收费模式。 “1”表示按照CU时收费。 “2”表示按照包年包月收费。

        :return: The charging_mode of this ShowQueueDetailResponse.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ShowQueueDetailResponse.

        队列的收费模式。 “1”表示按照CU时收费。 “2”表示按照包年包月收费。

        :param charging_mode: The charging_mode of this ShowQueueDetailResponse.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowQueueDetailResponse.

        队列的资源ID。

        :return: The resource_id of this ShowQueueDetailResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowQueueDetailResponse.

        队列的资源ID。

        :param resource_id: The resource_id of this ShowQueueDetailResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def queue_type(self):
        """Gets the queue_type of this ShowQueueDetailResponse.

        队列的资源ID。

        :return: The queue_type of this ShowQueueDetailResponse.
        :rtype: str
        """
        return self._queue_type

    @queue_type.setter
    def queue_type(self, queue_type):
        """Sets the queue_type of this ShowQueueDetailResponse.

        队列的资源ID。

        :param queue_type: The queue_type of this ShowQueueDetailResponse.
        :type queue_type: str
        """
        self._queue_type = queue_type

    @property
    def resource_type(self):
        """Gets the resource_type of this ShowQueueDetailResponse.

        队列的资源ID。

        :return: The resource_type of this ShowQueueDetailResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ShowQueueDetailResponse.

        队列的资源ID。

        :param resource_type: The resource_type of this ShowQueueDetailResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_mode(self):
        """Gets the resource_mode of this ShowQueueDetailResponse.

        队列类型。 0：共享队列 1：专属队列

        :return: The resource_mode of this ShowQueueDetailResponse.
        :rtype: int
        """
        return self._resource_mode

    @resource_mode.setter
    def resource_mode(self, resource_mode):
        """Sets the resource_mode of this ShowQueueDetailResponse.

        队列类型。 0：共享队列 1：专属队列

        :param resource_mode: The resource_mode of this ShowQueueDetailResponse.
        :type resource_mode: int
        """
        self._resource_mode = resource_mode

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowQueueDetailResponse.

        企业项目ID。\"0”表示default，即默认的企业项目。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :return: The enterprise_project_id of this ShowQueueDetailResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowQueueDetailResponse.

        企业项目ID。\"0”表示default，即默认的企业项目。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :param enterprise_project_id: The enterprise_project_id of this ShowQueueDetailResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cu_spec(self):
        """Gets the cu_spec of this ShowQueueDetailResponse.

        队列的规格大小。对于包周期队列，表示包周期部分的CU值；对于按需队列，表示用户购买队列时的初始值。

        :return: The cu_spec of this ShowQueueDetailResponse.
        :rtype: int
        """
        return self._cu_spec

    @cu_spec.setter
    def cu_spec(self, cu_spec):
        """Sets the cu_spec of this ShowQueueDetailResponse.

        队列的规格大小。对于包周期队列，表示包周期部分的CU值；对于按需队列，表示用户购买队列时的初始值。

        :param cu_spec: The cu_spec of this ShowQueueDetailResponse.
        :type cu_spec: int
        """
        self._cu_spec = cu_spec

    @property
    def cu_scale_out_limit(self):
        """Gets the cu_scale_out_limit of this ShowQueueDetailResponse.

        当前队列弹性扩缩容的CU值上限。

        :return: The cu_scale_out_limit of this ShowQueueDetailResponse.
        :rtype: int
        """
        return self._cu_scale_out_limit

    @cu_scale_out_limit.setter
    def cu_scale_out_limit(self, cu_scale_out_limit):
        """Sets the cu_scale_out_limit of this ShowQueueDetailResponse.

        当前队列弹性扩缩容的CU值上限。

        :param cu_scale_out_limit: The cu_scale_out_limit of this ShowQueueDetailResponse.
        :type cu_scale_out_limit: int
        """
        self._cu_scale_out_limit = cu_scale_out_limit

    @property
    def cu_scale_in_limit(self):
        """Gets the cu_scale_in_limit of this ShowQueueDetailResponse.

        当前队列弹性扩缩容的CU值下限。

        :return: The cu_scale_in_limit of this ShowQueueDetailResponse.
        :rtype: int
        """
        return self._cu_scale_in_limit

    @cu_scale_in_limit.setter
    def cu_scale_in_limit(self, cu_scale_in_limit):
        """Sets the cu_scale_in_limit of this ShowQueueDetailResponse.

        当前队列弹性扩缩容的CU值下限。

        :param cu_scale_in_limit: The cu_scale_in_limit of this ShowQueueDetailResponse.
        :type cu_scale_in_limit: int
        """
        self._cu_scale_in_limit = cu_scale_in_limit

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
        if not isinstance(other, ShowQueueDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
