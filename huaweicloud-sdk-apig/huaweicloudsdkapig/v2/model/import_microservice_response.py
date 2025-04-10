# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportMicroserviceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_channel_id': 'str',
        'api_group_id': 'str',
        'apis': 'list[MicroserviceImportApiResp]'
    }

    attribute_map = {
        'vpc_channel_id': 'vpc_channel_id',
        'api_group_id': 'api_group_id',
        'apis': 'apis'
    }

    def __init__(self, vpc_channel_id=None, api_group_id=None, apis=None):
        r"""ImportMicroserviceResponse

        The model defined in huaweicloud sdk

        :param vpc_channel_id: vpc通道编号
        :type vpc_channel_id: str
        :param api_group_id: api分组编号
        :type api_group_id: str
        :param apis: 导入的api列表
        :type apis: list[:class:`huaweicloudsdkapig.v2.MicroserviceImportApiResp`]
        """
        
        super(ImportMicroserviceResponse, self).__init__()

        self._vpc_channel_id = None
        self._api_group_id = None
        self._apis = None
        self.discriminator = None

        if vpc_channel_id is not None:
            self.vpc_channel_id = vpc_channel_id
        if api_group_id is not None:
            self.api_group_id = api_group_id
        if apis is not None:
            self.apis = apis

    @property
    def vpc_channel_id(self):
        r"""Gets the vpc_channel_id of this ImportMicroserviceResponse.

        vpc通道编号

        :return: The vpc_channel_id of this ImportMicroserviceResponse.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        r"""Sets the vpc_channel_id of this ImportMicroserviceResponse.

        vpc通道编号

        :param vpc_channel_id: The vpc_channel_id of this ImportMicroserviceResponse.
        :type vpc_channel_id: str
        """
        self._vpc_channel_id = vpc_channel_id

    @property
    def api_group_id(self):
        r"""Gets the api_group_id of this ImportMicroserviceResponse.

        api分组编号

        :return: The api_group_id of this ImportMicroserviceResponse.
        :rtype: str
        """
        return self._api_group_id

    @api_group_id.setter
    def api_group_id(self, api_group_id):
        r"""Sets the api_group_id of this ImportMicroserviceResponse.

        api分组编号

        :param api_group_id: The api_group_id of this ImportMicroserviceResponse.
        :type api_group_id: str
        """
        self._api_group_id = api_group_id

    @property
    def apis(self):
        r"""Gets the apis of this ImportMicroserviceResponse.

        导入的api列表

        :return: The apis of this ImportMicroserviceResponse.
        :rtype: list[:class:`huaweicloudsdkapig.v2.MicroserviceImportApiResp`]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        r"""Sets the apis of this ImportMicroserviceResponse.

        导入的api列表

        :param apis: The apis of this ImportMicroserviceResponse.
        :type apis: list[:class:`huaweicloudsdkapig.v2.MicroserviceImportApiResp`]
        """
        self._apis = apis

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
        if not isinstance(other, ImportMicroserviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
