# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionPersistence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cookie_name': 'str',
        'type': 'str',
        'persistence_timeout': 'int'
    }

    attribute_map = {
        'cookie_name': 'cookie_name',
        'type': 'type',
        'persistence_timeout': 'persistence_timeout'
    }

    def __init__(self, cookie_name=None, type=None, persistence_timeout=None):
        """SessionPersistence

        The model defined in huaweicloud sdk

        :param cookie_name: cookie名称。  格式：仅支持字母、数字、中划线(-)、下划线(_)和点号(.)。  使用说明： - 只有当type为APP_COOKIE时才有效。其他情况下传该字段会报错。  [不支持该字段，请勿使用。](tag:hws_eu,hcso_dt)
        :type cookie_name: str
        :param type: 会话保持类型。  取值范围：SOURCE_IP、HTTP_COOKIE、APP_COOKIE。  [使用说明： - 当pool的protocol为TCP、UDP，无论type取值如何，都会被忽略，会话保持只按SOURCE_IP生效。 - 当pool的protocol为HTTP、HTTPS时。如果是独享型负载均衡器的pool， 则type只能为HTTP_COOKIE，其他取值会话保持失效。 如果是共享型负载均衡器的pool，则type可以为HTTP_COOKIE和APP_COOKIE，其他取值会话保持失效。 - 若pool的protocol为QUIC，则必须开启session_persistence且type为SOURCE_IP。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt)  [使用说明： - 当pool的protocol为TCP、UDP，无论type取值如何，都会被忽略，会话保持只按SOURCE_IP生效。 - 当pool的protocol为HTTP、HTTPS时。type只能为HTTP_COOKIE， 其他取值会话保持失效。](tag:hws_eu,hcso_dt)
        :type type: str
        :param persistence_timeout: 会话保持的时间。当type为APP_COOKIE时不生效。  适用范围：如果pool的protocol为TCP、UDP和QUIC则范围为[1,60]（分钟），默认值1； 如果pool的protocol为HTTP和HTTPS则范围为[1,1440]（分钟），默认值1440。  [荷兰region不支持QUIC。](tag:dt)
        :type persistence_timeout: int
        """
        
        

        self._cookie_name = None
        self._type = None
        self._persistence_timeout = None
        self.discriminator = None

        if cookie_name is not None:
            self.cookie_name = cookie_name
        self.type = type
        if persistence_timeout is not None:
            self.persistence_timeout = persistence_timeout

    @property
    def cookie_name(self):
        """Gets the cookie_name of this SessionPersistence.

        cookie名称。  格式：仅支持字母、数字、中划线(-)、下划线(_)和点号(.)。  使用说明： - 只有当type为APP_COOKIE时才有效。其他情况下传该字段会报错。  [不支持该字段，请勿使用。](tag:hws_eu,hcso_dt)

        :return: The cookie_name of this SessionPersistence.
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        """Sets the cookie_name of this SessionPersistence.

        cookie名称。  格式：仅支持字母、数字、中划线(-)、下划线(_)和点号(.)。  使用说明： - 只有当type为APP_COOKIE时才有效。其他情况下传该字段会报错。  [不支持该字段，请勿使用。](tag:hws_eu,hcso_dt)

        :param cookie_name: The cookie_name of this SessionPersistence.
        :type cookie_name: str
        """
        self._cookie_name = cookie_name

    @property
    def type(self):
        """Gets the type of this SessionPersistence.

        会话保持类型。  取值范围：SOURCE_IP、HTTP_COOKIE、APP_COOKIE。  [使用说明： - 当pool的protocol为TCP、UDP，无论type取值如何，都会被忽略，会话保持只按SOURCE_IP生效。 - 当pool的protocol为HTTP、HTTPS时。如果是独享型负载均衡器的pool， 则type只能为HTTP_COOKIE，其他取值会话保持失效。 如果是共享型负载均衡器的pool，则type可以为HTTP_COOKIE和APP_COOKIE，其他取值会话保持失效。 - 若pool的protocol为QUIC，则必须开启session_persistence且type为SOURCE_IP。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt)  [使用说明： - 当pool的protocol为TCP、UDP，无论type取值如何，都会被忽略，会话保持只按SOURCE_IP生效。 - 当pool的protocol为HTTP、HTTPS时。type只能为HTTP_COOKIE， 其他取值会话保持失效。](tag:hws_eu,hcso_dt)

        :return: The type of this SessionPersistence.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SessionPersistence.

        会话保持类型。  取值范围：SOURCE_IP、HTTP_COOKIE、APP_COOKIE。  [使用说明： - 当pool的protocol为TCP、UDP，无论type取值如何，都会被忽略，会话保持只按SOURCE_IP生效。 - 当pool的protocol为HTTP、HTTPS时。如果是独享型负载均衡器的pool， 则type只能为HTTP_COOKIE，其他取值会话保持失效。 如果是共享型负载均衡器的pool，则type可以为HTTP_COOKIE和APP_COOKIE，其他取值会话保持失效。 - 若pool的protocol为QUIC，则必须开启session_persistence且type为SOURCE_IP。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt)  [使用说明： - 当pool的protocol为TCP、UDP，无论type取值如何，都会被忽略，会话保持只按SOURCE_IP生效。 - 当pool的protocol为HTTP、HTTPS时。type只能为HTTP_COOKIE， 其他取值会话保持失效。](tag:hws_eu,hcso_dt)

        :param type: The type of this SessionPersistence.
        :type type: str
        """
        self._type = type

    @property
    def persistence_timeout(self):
        """Gets the persistence_timeout of this SessionPersistence.

        会话保持的时间。当type为APP_COOKIE时不生效。  适用范围：如果pool的protocol为TCP、UDP和QUIC则范围为[1,60]（分钟），默认值1； 如果pool的protocol为HTTP和HTTPS则范围为[1,1440]（分钟），默认值1440。  [荷兰region不支持QUIC。](tag:dt)

        :return: The persistence_timeout of this SessionPersistence.
        :rtype: int
        """
        return self._persistence_timeout

    @persistence_timeout.setter
    def persistence_timeout(self, persistence_timeout):
        """Sets the persistence_timeout of this SessionPersistence.

        会话保持的时间。当type为APP_COOKIE时不生效。  适用范围：如果pool的protocol为TCP、UDP和QUIC则范围为[1,60]（分钟），默认值1； 如果pool的protocol为HTTP和HTTPS则范围为[1,1440]（分钟），默认值1440。  [荷兰region不支持QUIC。](tag:dt)

        :param persistence_timeout: The persistence_timeout of this SessionPersistence.
        :type persistence_timeout: int
        """
        self._persistence_timeout = persistence_timeout

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
        if not isinstance(other, SessionPersistence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
