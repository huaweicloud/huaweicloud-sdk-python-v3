# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkflowPurchasePoolResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'pool_id': 'str',
        'service_id': 'str',
        'workflow_id': 'str',
        'order': 'WorkflowPoolOrder',
        'consume_limit': 'int',
        'current_consume': 'int',
        'current_date': 'str',
        'limit_enable': 'bool',
        'created_at': 'str',
        'package_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'pool_id': 'pool_id',
        'service_id': 'service_id',
        'workflow_id': 'workflow_id',
        'order': 'order',
        'consume_limit': 'consume_limit',
        'current_consume': 'current_consume',
        'current_date': 'current_date',
        'limit_enable': 'limit_enable',
        'created_at': 'created_at',
        'package_id': 'package_id'
    }

    def __init__(self, status=None, pool_id=None, service_id=None, workflow_id=None, order=None, consume_limit=None, current_consume=None, current_date=None, limit_enable=None, created_at=None, package_id=None):
        r"""CreateWorkflowPurchasePoolResponse

        The model defined in huaweicloud sdk

        :param status: 服务包状态。
        :type status: str
        :param pool_id: 资源池ID。
        :type pool_id: str
        :param service_id: 在线服务ID。
        :type service_id: str
        :param workflow_id: Workflow工作流ID。
        :type workflow_id: str
        :param order: 
        :type order: :class:`huaweicloudsdkmodelarts.v1.WorkflowPoolOrder`
        :param consume_limit: 消费限制。
        :type consume_limit: int
        :param current_consume: 当前消费。
        :type current_consume: int
        :param current_date: 当前时间。
        :type current_date: str
        :param limit_enable: 限制开关。
        :type limit_enable: bool
        :param created_at: 创建时间。
        :type created_at: str
        :param package_id: 订阅包的UUID。创建时不需要填，由后台自动生成。
        :type package_id: str
        """
        
        super().__init__()

        self._status = None
        self._pool_id = None
        self._service_id = None
        self._workflow_id = None
        self._order = None
        self._consume_limit = None
        self._current_consume = None
        self._current_date = None
        self._limit_enable = None
        self._created_at = None
        self._package_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if pool_id is not None:
            self.pool_id = pool_id
        if service_id is not None:
            self.service_id = service_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if order is not None:
            self.order = order
        if consume_limit is not None:
            self.consume_limit = consume_limit
        if current_consume is not None:
            self.current_consume = current_consume
        if current_date is not None:
            self.current_date = current_date
        if limit_enable is not None:
            self.limit_enable = limit_enable
        if created_at is not None:
            self.created_at = created_at
        if package_id is not None:
            self.package_id = package_id

    @property
    def status(self):
        r"""Gets the status of this CreateWorkflowPurchasePoolResponse.

        服务包状态。

        :return: The status of this CreateWorkflowPurchasePoolResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateWorkflowPurchasePoolResponse.

        服务包状态。

        :param status: The status of this CreateWorkflowPurchasePoolResponse.
        :type status: str
        """
        self._status = status

    @property
    def pool_id(self):
        r"""Gets the pool_id of this CreateWorkflowPurchasePoolResponse.

        资源池ID。

        :return: The pool_id of this CreateWorkflowPurchasePoolResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this CreateWorkflowPurchasePoolResponse.

        资源池ID。

        :param pool_id: The pool_id of this CreateWorkflowPurchasePoolResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def service_id(self):
        r"""Gets the service_id of this CreateWorkflowPurchasePoolResponse.

        在线服务ID。

        :return: The service_id of this CreateWorkflowPurchasePoolResponse.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this CreateWorkflowPurchasePoolResponse.

        在线服务ID。

        :param service_id: The service_id of this CreateWorkflowPurchasePoolResponse.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this CreateWorkflowPurchasePoolResponse.

        Workflow工作流ID。

        :return: The workflow_id of this CreateWorkflowPurchasePoolResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this CreateWorkflowPurchasePoolResponse.

        Workflow工作流ID。

        :param workflow_id: The workflow_id of this CreateWorkflowPurchasePoolResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def order(self):
        r"""Gets the order of this CreateWorkflowPurchasePoolResponse.

        :return: The order of this CreateWorkflowPurchasePoolResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowPoolOrder`
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this CreateWorkflowPurchasePoolResponse.

        :param order: The order of this CreateWorkflowPurchasePoolResponse.
        :type order: :class:`huaweicloudsdkmodelarts.v1.WorkflowPoolOrder`
        """
        self._order = order

    @property
    def consume_limit(self):
        r"""Gets the consume_limit of this CreateWorkflowPurchasePoolResponse.

        消费限制。

        :return: The consume_limit of this CreateWorkflowPurchasePoolResponse.
        :rtype: int
        """
        return self._consume_limit

    @consume_limit.setter
    def consume_limit(self, consume_limit):
        r"""Sets the consume_limit of this CreateWorkflowPurchasePoolResponse.

        消费限制。

        :param consume_limit: The consume_limit of this CreateWorkflowPurchasePoolResponse.
        :type consume_limit: int
        """
        self._consume_limit = consume_limit

    @property
    def current_consume(self):
        r"""Gets the current_consume of this CreateWorkflowPurchasePoolResponse.

        当前消费。

        :return: The current_consume of this CreateWorkflowPurchasePoolResponse.
        :rtype: int
        """
        return self._current_consume

    @current_consume.setter
    def current_consume(self, current_consume):
        r"""Sets the current_consume of this CreateWorkflowPurchasePoolResponse.

        当前消费。

        :param current_consume: The current_consume of this CreateWorkflowPurchasePoolResponse.
        :type current_consume: int
        """
        self._current_consume = current_consume

    @property
    def current_date(self):
        r"""Gets the current_date of this CreateWorkflowPurchasePoolResponse.

        当前时间。

        :return: The current_date of this CreateWorkflowPurchasePoolResponse.
        :rtype: str
        """
        return self._current_date

    @current_date.setter
    def current_date(self, current_date):
        r"""Sets the current_date of this CreateWorkflowPurchasePoolResponse.

        当前时间。

        :param current_date: The current_date of this CreateWorkflowPurchasePoolResponse.
        :type current_date: str
        """
        self._current_date = current_date

    @property
    def limit_enable(self):
        r"""Gets the limit_enable of this CreateWorkflowPurchasePoolResponse.

        限制开关。

        :return: The limit_enable of this CreateWorkflowPurchasePoolResponse.
        :rtype: bool
        """
        return self._limit_enable

    @limit_enable.setter
    def limit_enable(self, limit_enable):
        r"""Sets the limit_enable of this CreateWorkflowPurchasePoolResponse.

        限制开关。

        :param limit_enable: The limit_enable of this CreateWorkflowPurchasePoolResponse.
        :type limit_enable: bool
        """
        self._limit_enable = limit_enable

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateWorkflowPurchasePoolResponse.

        创建时间。

        :return: The created_at of this CreateWorkflowPurchasePoolResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateWorkflowPurchasePoolResponse.

        创建时间。

        :param created_at: The created_at of this CreateWorkflowPurchasePoolResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def package_id(self):
        r"""Gets the package_id of this CreateWorkflowPurchasePoolResponse.

        订阅包的UUID。创建时不需要填，由后台自动生成。

        :return: The package_id of this CreateWorkflowPurchasePoolResponse.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        r"""Sets the package_id of this CreateWorkflowPurchasePoolResponse.

        订阅包的UUID。创建时不需要填，由后台自动生成。

        :param package_id: The package_id of this CreateWorkflowPurchasePoolResponse.
        :type package_id: str
        """
        self._package_id = package_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateWorkflowPurchasePoolResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateWorkflowPurchasePoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
