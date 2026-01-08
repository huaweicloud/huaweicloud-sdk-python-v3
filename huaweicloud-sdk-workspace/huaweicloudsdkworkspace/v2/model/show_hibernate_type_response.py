# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHibernateTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'hibernate_type': 'str',
        'shutdown_days': 'int'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'hibernate_type': 'hibernate_type',
        'shutdown_days': 'shutdown_days'
    }

    def __init__(self, tenant_id=None, hibernate_type=None, shutdown_days=None):
        r"""ShowHibernateTypeResponse

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id
        :type tenant_id: str
        :param hibernate_type: ECS休眠类型 - SUSPEND: 带外冷休眠 - PAUSE: 带外热休眠
        :type hibernate_type: str
        :param shutdown_days: 休眠关机时长（天）
        :type shutdown_days: int
        """
        
        super().__init__()

        self._tenant_id = None
        self._hibernate_type = None
        self._shutdown_days = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if hibernate_type is not None:
            self.hibernate_type = hibernate_type
        if shutdown_days is not None:
            self.shutdown_days = shutdown_days

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowHibernateTypeResponse.

        租户id

        :return: The tenant_id of this ShowHibernateTypeResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowHibernateTypeResponse.

        租户id

        :param tenant_id: The tenant_id of this ShowHibernateTypeResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def hibernate_type(self):
        r"""Gets the hibernate_type of this ShowHibernateTypeResponse.

        ECS休眠类型 - SUSPEND: 带外冷休眠 - PAUSE: 带外热休眠

        :return: The hibernate_type of this ShowHibernateTypeResponse.
        :rtype: str
        """
        return self._hibernate_type

    @hibernate_type.setter
    def hibernate_type(self, hibernate_type):
        r"""Sets the hibernate_type of this ShowHibernateTypeResponse.

        ECS休眠类型 - SUSPEND: 带外冷休眠 - PAUSE: 带外热休眠

        :param hibernate_type: The hibernate_type of this ShowHibernateTypeResponse.
        :type hibernate_type: str
        """
        self._hibernate_type = hibernate_type

    @property
    def shutdown_days(self):
        r"""Gets the shutdown_days of this ShowHibernateTypeResponse.

        休眠关机时长（天）

        :return: The shutdown_days of this ShowHibernateTypeResponse.
        :rtype: int
        """
        return self._shutdown_days

    @shutdown_days.setter
    def shutdown_days(self, shutdown_days):
        r"""Sets the shutdown_days of this ShowHibernateTypeResponse.

        休眠关机时长（天）

        :param shutdown_days: The shutdown_days of this ShowHibernateTypeResponse.
        :type shutdown_days: int
        """
        self._shutdown_days = shutdown_days

    def to_dict(self):
        import warnings
        warnings.warn("ShowHibernateTypeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowHibernateTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
