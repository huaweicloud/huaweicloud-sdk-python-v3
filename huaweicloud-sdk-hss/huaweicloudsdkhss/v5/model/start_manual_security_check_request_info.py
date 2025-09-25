# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartManualSecurityCheckRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'list[str]',
        'host_id_list': 'list[str]',
        'operate_all': 'bool'
    }

    attribute_map = {
        'content': 'content',
        'host_id_list': 'host_id_list',
        'operate_all': 'operate_all'
    }

    def __init__(self, content=None, host_id_list=None, operate_all=None):
        r"""StartManualSecurityCheckRequestInfo

        The model defined in huaweicloud sdk

        :param content: 体检内容，取值包含：asset,vul,baseline,event
        :type content: list[str]
        :param host_id_list: 已选服务器ID列表
        :type host_id_list: list[str]
        :param operate_all: 服务器是否选择全部，全选跟查询条件无关
        :type operate_all: bool
        """
        
        

        self._content = None
        self._host_id_list = None
        self._operate_all = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if host_id_list is not None:
            self.host_id_list = host_id_list
        if operate_all is not None:
            self.operate_all = operate_all

    @property
    def content(self):
        r"""Gets the content of this StartManualSecurityCheckRequestInfo.

        体检内容，取值包含：asset,vul,baseline,event

        :return: The content of this StartManualSecurityCheckRequestInfo.
        :rtype: list[str]
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this StartManualSecurityCheckRequestInfo.

        体检内容，取值包含：asset,vul,baseline,event

        :param content: The content of this StartManualSecurityCheckRequestInfo.
        :type content: list[str]
        """
        self._content = content

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this StartManualSecurityCheckRequestInfo.

        已选服务器ID列表

        :return: The host_id_list of this StartManualSecurityCheckRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this StartManualSecurityCheckRequestInfo.

        已选服务器ID列表

        :param host_id_list: The host_id_list of this StartManualSecurityCheckRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def operate_all(self):
        r"""Gets the operate_all of this StartManualSecurityCheckRequestInfo.

        服务器是否选择全部，全选跟查询条件无关

        :return: The operate_all of this StartManualSecurityCheckRequestInfo.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        r"""Sets the operate_all of this StartManualSecurityCheckRequestInfo.

        服务器是否选择全部，全选跟查询条件无关

        :param operate_all: The operate_all of this StartManualSecurityCheckRequestInfo.
        :type operate_all: bool
        """
        self._operate_all = operate_all

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
        if not isinstance(other, StartManualSecurityCheckRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
