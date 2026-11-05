# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSupabaseApplicationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'job_id': 'str',
        'application_id': 'str',
        'instance_id': 'str',
        'instance_job_id': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'job_id': 'job_id',
        'application_id': 'application_id',
        'instance_id': 'instance_id',
        'instance_job_id': 'instance_job_id'
    }

    def __init__(self, order_id=None, job_id=None, application_id=None, instance_id=None, instance_job_id=None):
        r"""CreateSupabaseApplicationResponse

        The model defined in huaweicloud sdk

        :param order_id: 订单ID（包周期时返回）。
        :type order_id: str
        :param job_id: 应用创建任务ID。
        :type job_id: str
        :param application_id: Supabase应用ID。
        :type application_id: str
        :param instance_id: 数据库实例ID。
        :type instance_id: str
        :param instance_job_id: 实例创建任务ID。
        :type instance_job_id: str
        """
        
        super().__init__()

        self._order_id = None
        self._job_id = None
        self._application_id = None
        self._instance_id = None
        self._instance_job_id = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if job_id is not None:
            self.job_id = job_id
        if application_id is not None:
            self.application_id = application_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_job_id is not None:
            self.instance_job_id = instance_job_id

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateSupabaseApplicationResponse.

        订单ID（包周期时返回）。

        :return: The order_id of this CreateSupabaseApplicationResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateSupabaseApplicationResponse.

        订单ID（包周期时返回）。

        :param order_id: The order_id of this CreateSupabaseApplicationResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateSupabaseApplicationResponse.

        应用创建任务ID。

        :return: The job_id of this CreateSupabaseApplicationResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateSupabaseApplicationResponse.

        应用创建任务ID。

        :param job_id: The job_id of this CreateSupabaseApplicationResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def application_id(self):
        r"""Gets the application_id of this CreateSupabaseApplicationResponse.

        Supabase应用ID。

        :return: The application_id of this CreateSupabaseApplicationResponse.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this CreateSupabaseApplicationResponse.

        Supabase应用ID。

        :param application_id: The application_id of this CreateSupabaseApplicationResponse.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateSupabaseApplicationResponse.

        数据库实例ID。

        :return: The instance_id of this CreateSupabaseApplicationResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateSupabaseApplicationResponse.

        数据库实例ID。

        :param instance_id: The instance_id of this CreateSupabaseApplicationResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_job_id(self):
        r"""Gets the instance_job_id of this CreateSupabaseApplicationResponse.

        实例创建任务ID。

        :return: The instance_job_id of this CreateSupabaseApplicationResponse.
        :rtype: str
        """
        return self._instance_job_id

    @instance_job_id.setter
    def instance_job_id(self, instance_job_id):
        r"""Sets the instance_job_id of this CreateSupabaseApplicationResponse.

        实例创建任务ID。

        :param instance_job_id: The instance_job_id of this CreateSupabaseApplicationResponse.
        :type instance_job_id: str
        """
        self._instance_job_id = instance_job_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateSupabaseApplicationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateSupabaseApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
