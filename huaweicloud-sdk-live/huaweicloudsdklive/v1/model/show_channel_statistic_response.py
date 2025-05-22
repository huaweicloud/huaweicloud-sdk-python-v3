# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowChannelStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'id': 'str',
        'type': 'str',
        'scte35': 'SCTE35StatisticRsp'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'id': 'id',
        'type': 'type',
        'scte35': 'scte35'
    }

    def __init__(self, domain=None, app_name=None, id=None, type=None, scte35=None):
        r"""ShowChannelStatisticResponse

        The model defined in huaweicloud sdk

        :param domain: 频道推流域名。
        :type domain: str
        :param app_name: 组名或应用名。
        :type app_name: str
        :param id: 频道ID。频道唯一标识，为必填项。
        :type id: str
        :param type: 统计信息的类型，scte35。
        :type type: str
        :param scte35: 
        :type scte35: :class:`huaweicloudsdklive.v1.SCTE35StatisticRsp`
        """
        
        super(ShowChannelStatisticResponse, self).__init__()

        self._domain = None
        self._app_name = None
        self._id = None
        self._type = None
        self._scte35 = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if app_name is not None:
            self.app_name = app_name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if scte35 is not None:
            self.scte35 = scte35

    @property
    def domain(self):
        r"""Gets the domain of this ShowChannelStatisticResponse.

        频道推流域名。

        :return: The domain of this ShowChannelStatisticResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ShowChannelStatisticResponse.

        频道推流域名。

        :param domain: The domain of this ShowChannelStatisticResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this ShowChannelStatisticResponse.

        组名或应用名。

        :return: The app_name of this ShowChannelStatisticResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ShowChannelStatisticResponse.

        组名或应用名。

        :param app_name: The app_name of this ShowChannelStatisticResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this ShowChannelStatisticResponse.

        频道ID。频道唯一标识，为必填项。

        :return: The id of this ShowChannelStatisticResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowChannelStatisticResponse.

        频道ID。频道唯一标识，为必填项。

        :param id: The id of this ShowChannelStatisticResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ShowChannelStatisticResponse.

        统计信息的类型，scte35。

        :return: The type of this ShowChannelStatisticResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowChannelStatisticResponse.

        统计信息的类型，scte35。

        :param type: The type of this ShowChannelStatisticResponse.
        :type type: str
        """
        self._type = type

    @property
    def scte35(self):
        r"""Gets the scte35 of this ShowChannelStatisticResponse.

        :return: The scte35 of this ShowChannelStatisticResponse.
        :rtype: :class:`huaweicloudsdklive.v1.SCTE35StatisticRsp`
        """
        return self._scte35

    @scte35.setter
    def scte35(self, scte35):
        r"""Sets the scte35 of this ShowChannelStatisticResponse.

        :param scte35: The scte35 of this ShowChannelStatisticResponse.
        :type scte35: :class:`huaweicloudsdklive.v1.SCTE35StatisticRsp`
        """
        self._scte35 = scte35

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
        if not isinstance(other, ShowChannelStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
