# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAntiDDosServiceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_type_id': 'int',
        'cleaning_access_pos_id': 'int',
        'enable_l7': 'bool',
        'http_request_pos_id': 'int',
        'traffic_pos_id': 'int'
    }

    attribute_map = {
        'app_type_id': 'app_type_id',
        'cleaning_access_pos_id': 'cleaning_access_pos_id',
        'enable_l7': 'enable_L7',
        'http_request_pos_id': 'http_request_pos_id',
        'traffic_pos_id': 'traffic_pos_id'
    }

    def __init__(self, app_type_id=None, cleaning_access_pos_id=None, enable_l7=None, http_request_pos_id=None, traffic_pos_id=None):
        """UpdateAntiDDosServiceRequestBody

        The model defined in huaweicloud sdk

        :param app_type_id: 应用类型ID，可选取值： - 0 - 1
        :type app_type_id: int
        :param cleaning_access_pos_id: 清洗时访问限制分段ID，取值范围：1～8
        :type cleaning_access_pos_id: int
        :param enable_l7: 是否开启L7层防护
        :type enable_l7: bool
        :param http_request_pos_id: HTTP请求数分段ID，取值范围：1～15
        :type http_request_pos_id: int
        :param traffic_pos_id: 流量分段ID，取值范围：1～9
        :type traffic_pos_id: int
        """
        
        

        self._app_type_id = None
        self._cleaning_access_pos_id = None
        self._enable_l7 = None
        self._http_request_pos_id = None
        self._traffic_pos_id = None
        self.discriminator = None

        self.app_type_id = app_type_id
        self.cleaning_access_pos_id = cleaning_access_pos_id
        self.enable_l7 = enable_l7
        self.http_request_pos_id = http_request_pos_id
        self.traffic_pos_id = traffic_pos_id

    @property
    def app_type_id(self):
        """Gets the app_type_id of this UpdateAntiDDosServiceRequestBody.

        应用类型ID，可选取值： - 0 - 1

        :return: The app_type_id of this UpdateAntiDDosServiceRequestBody.
        :rtype: int
        """
        return self._app_type_id

    @app_type_id.setter
    def app_type_id(self, app_type_id):
        """Sets the app_type_id of this UpdateAntiDDosServiceRequestBody.

        应用类型ID，可选取值： - 0 - 1

        :param app_type_id: The app_type_id of this UpdateAntiDDosServiceRequestBody.
        :type app_type_id: int
        """
        self._app_type_id = app_type_id

    @property
    def cleaning_access_pos_id(self):
        """Gets the cleaning_access_pos_id of this UpdateAntiDDosServiceRequestBody.

        清洗时访问限制分段ID，取值范围：1～8

        :return: The cleaning_access_pos_id of this UpdateAntiDDosServiceRequestBody.
        :rtype: int
        """
        return self._cleaning_access_pos_id

    @cleaning_access_pos_id.setter
    def cleaning_access_pos_id(self, cleaning_access_pos_id):
        """Sets the cleaning_access_pos_id of this UpdateAntiDDosServiceRequestBody.

        清洗时访问限制分段ID，取值范围：1～8

        :param cleaning_access_pos_id: The cleaning_access_pos_id of this UpdateAntiDDosServiceRequestBody.
        :type cleaning_access_pos_id: int
        """
        self._cleaning_access_pos_id = cleaning_access_pos_id

    @property
    def enable_l7(self):
        """Gets the enable_l7 of this UpdateAntiDDosServiceRequestBody.

        是否开启L7层防护

        :return: The enable_l7 of this UpdateAntiDDosServiceRequestBody.
        :rtype: bool
        """
        return self._enable_l7

    @enable_l7.setter
    def enable_l7(self, enable_l7):
        """Sets the enable_l7 of this UpdateAntiDDosServiceRequestBody.

        是否开启L7层防护

        :param enable_l7: The enable_l7 of this UpdateAntiDDosServiceRequestBody.
        :type enable_l7: bool
        """
        self._enable_l7 = enable_l7

    @property
    def http_request_pos_id(self):
        """Gets the http_request_pos_id of this UpdateAntiDDosServiceRequestBody.

        HTTP请求数分段ID，取值范围：1～15

        :return: The http_request_pos_id of this UpdateAntiDDosServiceRequestBody.
        :rtype: int
        """
        return self._http_request_pos_id

    @http_request_pos_id.setter
    def http_request_pos_id(self, http_request_pos_id):
        """Sets the http_request_pos_id of this UpdateAntiDDosServiceRequestBody.

        HTTP请求数分段ID，取值范围：1～15

        :param http_request_pos_id: The http_request_pos_id of this UpdateAntiDDosServiceRequestBody.
        :type http_request_pos_id: int
        """
        self._http_request_pos_id = http_request_pos_id

    @property
    def traffic_pos_id(self):
        """Gets the traffic_pos_id of this UpdateAntiDDosServiceRequestBody.

        流量分段ID，取值范围：1～9

        :return: The traffic_pos_id of this UpdateAntiDDosServiceRequestBody.
        :rtype: int
        """
        return self._traffic_pos_id

    @traffic_pos_id.setter
    def traffic_pos_id(self, traffic_pos_id):
        """Sets the traffic_pos_id of this UpdateAntiDDosServiceRequestBody.

        流量分段ID，取值范围：1～9

        :param traffic_pos_id: The traffic_pos_id of this UpdateAntiDDosServiceRequestBody.
        :type traffic_pos_id: int
        """
        self._traffic_pos_id = traffic_pos_id

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
        if not isinstance(other, UpdateAntiDDosServiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
