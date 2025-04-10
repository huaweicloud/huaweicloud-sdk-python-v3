# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_key': 'str',
        'app_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'flow_status': 'str',
        'has_variable': 'str',
        'region': 'str',
        'sign_name': 'str',
        'sort_dir': 'str',
        'sort_key': 'str',
        'template_id': 'str',
        'template_name': 'str',
        'template_type': 'str'
    }

    attribute_map = {
        'app_key': 'app_key',
        'app_name': 'app_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'flow_status': 'flow_status',
        'has_variable': 'has_variable',
        'region': 'region',
        'sign_name': 'sign_name',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type'
    }

    def __init__(self, app_key=None, app_name=None, start_time=None, end_time=None, limit=None, offset=None, flow_status=None, has_variable=None, region=None, sign_name=None, sort_dir=None, sort_key=None, template_id=None, template_name=None, template_type=None):
        r"""ListTemplateDetailsRequest

        The model defined in huaweicloud sdk

        :param app_key: 应用key
        :type app_key: str
        :param app_name: 应用名称
        :type app_name: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param limit: 数量
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param flow_status: 流程状态 1. Adopted: 通过 2. Reviewing: 审核中 3. Reject: 拒绝
        :type flow_status: str
        :param has_variable: 是否存在变量
        :type has_variable: str
        :param region: 地域 1. cn：国内 2. intl：国际
        :type region: str
        :param sign_name: 签名名称
        :type sign_name: str
        :param sort_dir: 排序方式 1. desc：降序 2. asc：升序
        :type sort_dir: str
        :param sort_key: 排序字段
        :type sort_key: str
        :param template_id: 模板ID
        :type template_id: str
        :param template_name: 模板名称
        :type template_name: str
        :param template_type: 模板类型 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类
        :type template_type: str
        """
        
        

        self._app_key = None
        self._app_name = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._flow_status = None
        self._has_variable = None
        self._region = None
        self._sign_name = None
        self._sort_dir = None
        self._sort_key = None
        self._template_id = None
        self._template_name = None
        self._template_type = None
        self.discriminator = None

        if app_key is not None:
            self.app_key = app_key
        if app_name is not None:
            self.app_name = app_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if flow_status is not None:
            self.flow_status = flow_status
        if has_variable is not None:
            self.has_variable = has_variable
        if region is not None:
            self.region = region
        if sign_name is not None:
            self.sign_name = sign_name
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if template_type is not None:
            self.template_type = template_type

    @property
    def app_key(self):
        r"""Gets the app_key of this ListTemplateDetailsRequest.

        应用key

        :return: The app_key of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this ListTemplateDetailsRequest.

        应用key

        :param app_key: The app_key of this ListTemplateDetailsRequest.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def app_name(self):
        r"""Gets the app_name of this ListTemplateDetailsRequest.

        应用名称

        :return: The app_name of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListTemplateDetailsRequest.

        应用名称

        :param app_name: The app_name of this ListTemplateDetailsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTemplateDetailsRequest.

        开始时间

        :return: The start_time of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTemplateDetailsRequest.

        开始时间

        :param start_time: The start_time of this ListTemplateDetailsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTemplateDetailsRequest.

        结束时间

        :return: The end_time of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTemplateDetailsRequest.

        结束时间

        :param end_time: The end_time of this ListTemplateDetailsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListTemplateDetailsRequest.

        数量

        :return: The limit of this ListTemplateDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTemplateDetailsRequest.

        数量

        :param limit: The limit of this ListTemplateDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTemplateDetailsRequest.

        偏移量

        :return: The offset of this ListTemplateDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTemplateDetailsRequest.

        偏移量

        :param offset: The offset of this ListTemplateDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def flow_status(self):
        r"""Gets the flow_status of this ListTemplateDetailsRequest.

        流程状态 1. Adopted: 通过 2. Reviewing: 审核中 3. Reject: 拒绝

        :return: The flow_status of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._flow_status

    @flow_status.setter
    def flow_status(self, flow_status):
        r"""Sets the flow_status of this ListTemplateDetailsRequest.

        流程状态 1. Adopted: 通过 2. Reviewing: 审核中 3. Reject: 拒绝

        :param flow_status: The flow_status of this ListTemplateDetailsRequest.
        :type flow_status: str
        """
        self._flow_status = flow_status

    @property
    def has_variable(self):
        r"""Gets the has_variable of this ListTemplateDetailsRequest.

        是否存在变量

        :return: The has_variable of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._has_variable

    @has_variable.setter
    def has_variable(self, has_variable):
        r"""Sets the has_variable of this ListTemplateDetailsRequest.

        是否存在变量

        :param has_variable: The has_variable of this ListTemplateDetailsRequest.
        :type has_variable: str
        """
        self._has_variable = has_variable

    @property
    def region(self):
        r"""Gets the region of this ListTemplateDetailsRequest.

        地域 1. cn：国内 2. intl：国际

        :return: The region of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListTemplateDetailsRequest.

        地域 1. cn：国内 2. intl：国际

        :param region: The region of this ListTemplateDetailsRequest.
        :type region: str
        """
        self._region = region

    @property
    def sign_name(self):
        r"""Gets the sign_name of this ListTemplateDetailsRequest.

        签名名称

        :return: The sign_name of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._sign_name

    @sign_name.setter
    def sign_name(self, sign_name):
        r"""Sets the sign_name of this ListTemplateDetailsRequest.

        签名名称

        :param sign_name: The sign_name of this ListTemplateDetailsRequest.
        :type sign_name: str
        """
        self._sign_name = sign_name

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListTemplateDetailsRequest.

        排序方式 1. desc：降序 2. asc：升序

        :return: The sort_dir of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListTemplateDetailsRequest.

        排序方式 1. desc：降序 2. asc：升序

        :param sort_dir: The sort_dir of this ListTemplateDetailsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListTemplateDetailsRequest.

        排序字段

        :return: The sort_key of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListTemplateDetailsRequest.

        排序字段

        :param sort_key: The sort_key of this ListTemplateDetailsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def template_id(self):
        r"""Gets the template_id of this ListTemplateDetailsRequest.

        模板ID

        :return: The template_id of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ListTemplateDetailsRequest.

        模板ID

        :param template_id: The template_id of this ListTemplateDetailsRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this ListTemplateDetailsRequest.

        模板名称

        :return: The template_name of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ListTemplateDetailsRequest.

        模板名称

        :param template_name: The template_name of this ListTemplateDetailsRequest.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this ListTemplateDetailsRequest.

        模板类型 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类

        :return: The template_type of this ListTemplateDetailsRequest.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this ListTemplateDetailsRequest.

        模板类型 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类

        :param template_type: The template_type of this ListTemplateDetailsRequest.
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
        if not isinstance(other, ListTemplateDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
