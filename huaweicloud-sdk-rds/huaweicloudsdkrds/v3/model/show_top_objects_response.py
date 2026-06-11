# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cur_time': 'int',
        'top_object_list': 'list[TopObject]',
        'top_object_overview_list': 'list[TopObjectOverview]'
    }

    attribute_map = {
        'cur_time': 'cur_time',
        'top_object_list': 'top_object_list',
        'top_object_overview_list': 'top_object_overview_list'
    }

    def __init__(self, cur_time=None, top_object_list=None, top_object_overview_list=None):
        r"""ShowTopObjectsResponse

        The model defined in huaweicloud sdk

        :param cur_time: 更新时间
        :type cur_time: int
        :param top_object_list: 明细
        :type top_object_list: list[:class:`huaweicloudsdkrds.v3.TopObject`]
        :param top_object_overview_list: 总览
        :type top_object_overview_list: list[:class:`huaweicloudsdkrds.v3.TopObjectOverview`]
        """
        
        super().__init__()

        self._cur_time = None
        self._top_object_list = None
        self._top_object_overview_list = None
        self.discriminator = None

        if cur_time is not None:
            self.cur_time = cur_time
        if top_object_list is not None:
            self.top_object_list = top_object_list
        if top_object_overview_list is not None:
            self.top_object_overview_list = top_object_overview_list

    @property
    def cur_time(self):
        r"""Gets the cur_time of this ShowTopObjectsResponse.

        更新时间

        :return: The cur_time of this ShowTopObjectsResponse.
        :rtype: int
        """
        return self._cur_time

    @cur_time.setter
    def cur_time(self, cur_time):
        r"""Sets the cur_time of this ShowTopObjectsResponse.

        更新时间

        :param cur_time: The cur_time of this ShowTopObjectsResponse.
        :type cur_time: int
        """
        self._cur_time = cur_time

    @property
    def top_object_list(self):
        r"""Gets the top_object_list of this ShowTopObjectsResponse.

        明细

        :return: The top_object_list of this ShowTopObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopObject`]
        """
        return self._top_object_list

    @top_object_list.setter
    def top_object_list(self, top_object_list):
        r"""Sets the top_object_list of this ShowTopObjectsResponse.

        明细

        :param top_object_list: The top_object_list of this ShowTopObjectsResponse.
        :type top_object_list: list[:class:`huaweicloudsdkrds.v3.TopObject`]
        """
        self._top_object_list = top_object_list

    @property
    def top_object_overview_list(self):
        r"""Gets the top_object_overview_list of this ShowTopObjectsResponse.

        总览

        :return: The top_object_overview_list of this ShowTopObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopObjectOverview`]
        """
        return self._top_object_overview_list

    @top_object_overview_list.setter
    def top_object_overview_list(self, top_object_overview_list):
        r"""Sets the top_object_overview_list of this ShowTopObjectsResponse.

        总览

        :param top_object_overview_list: The top_object_overview_list of this ShowTopObjectsResponse.
        :type top_object_overview_list: list[:class:`huaweicloudsdkrds.v3.TopObjectOverview`]
        """
        self._top_object_overview_list = top_object_overview_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowTopObjectsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTopObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
