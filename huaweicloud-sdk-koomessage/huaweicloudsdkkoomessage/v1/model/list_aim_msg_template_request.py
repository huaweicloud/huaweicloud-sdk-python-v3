# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimMsgTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'app_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'flow_status': 'str',
        'template_id': 'str',
        'template_name': 'str',
        'template_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'app_name': 'app_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'flow_status': 'flow_status',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type'
    }

    def __init__(self, offset=None, limit=None, app_name=None, start_time=None, end_time=None, flow_status=None, template_id=None, template_name=None, template_type=None):
        r"""ListAimMsgTemplateRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量。表示从偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param app_name: 应用名称。
        :type app_name: str
        :param start_time: 开始时间。
        :type start_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param flow_status: 流程状态。
        :type flow_status: str
        :param template_id: 模板ID。
        :type template_id: str
        :param template_name: 模板名称。
        :type template_name: str
        :param template_type: 模板类型。
        :type template_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._app_name = None
        self._start_time = None
        self._end_time = None
        self._flow_status = None
        self._template_id = None
        self._template_name = None
        self._template_type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if app_name is not None:
            self.app_name = app_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if flow_status is not None:
            self.flow_status = flow_status
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if template_type is not None:
            self.template_type = template_type

    @property
    def offset(self):
        r"""Gets the offset of this ListAimMsgTemplateRequest.

        偏移量。表示从偏移量开始查询，offset大于等于0。

        :return: The offset of this ListAimMsgTemplateRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAimMsgTemplateRequest.

        偏移量。表示从偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListAimMsgTemplateRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAimMsgTemplateRequest.

        每页显示的条目数量。

        :return: The limit of this ListAimMsgTemplateRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAimMsgTemplateRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListAimMsgTemplateRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def app_name(self):
        r"""Gets the app_name of this ListAimMsgTemplateRequest.

        应用名称。

        :return: The app_name of this ListAimMsgTemplateRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListAimMsgTemplateRequest.

        应用名称。

        :param app_name: The app_name of this ListAimMsgTemplateRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ListAimMsgTemplateRequest.

        开始时间。

        :return: The start_time of this ListAimMsgTemplateRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListAimMsgTemplateRequest.

        开始时间。

        :param start_time: The start_time of this ListAimMsgTemplateRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAimMsgTemplateRequest.

        结束时间。

        :return: The end_time of this ListAimMsgTemplateRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAimMsgTemplateRequest.

        结束时间。

        :param end_time: The end_time of this ListAimMsgTemplateRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def flow_status(self):
        r"""Gets the flow_status of this ListAimMsgTemplateRequest.

        流程状态。

        :return: The flow_status of this ListAimMsgTemplateRequest.
        :rtype: str
        """
        return self._flow_status

    @flow_status.setter
    def flow_status(self, flow_status):
        r"""Sets the flow_status of this ListAimMsgTemplateRequest.

        流程状态。

        :param flow_status: The flow_status of this ListAimMsgTemplateRequest.
        :type flow_status: str
        """
        self._flow_status = flow_status

    @property
    def template_id(self):
        r"""Gets the template_id of this ListAimMsgTemplateRequest.

        模板ID。

        :return: The template_id of this ListAimMsgTemplateRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ListAimMsgTemplateRequest.

        模板ID。

        :param template_id: The template_id of this ListAimMsgTemplateRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this ListAimMsgTemplateRequest.

        模板名称。

        :return: The template_name of this ListAimMsgTemplateRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ListAimMsgTemplateRequest.

        模板名称。

        :param template_name: The template_name of this ListAimMsgTemplateRequest.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this ListAimMsgTemplateRequest.

        模板类型。

        :return: The template_type of this ListAimMsgTemplateRequest.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this ListAimMsgTemplateRequest.

        模板类型。

        :param template_type: The template_type of this ListAimMsgTemplateRequest.
        :type template_type: str
        """
        self._template_type = template_type

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
        if not isinstance(other, ListAimMsgTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
