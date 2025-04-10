# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSignatureDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'signature_id': 'str',
        'signature_name': 'str',
        'signature_type': 'str',
        'site': 'str',
        'sort_dir': 'str',
        'sort_key': 'str',
        'status': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'signature_id': 'signature_id',
        'signature_name': 'signature_name',
        'signature_type': 'signature_type',
        'site': 'site',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'status': 'status'
    }

    def __init__(self, app_name=None, start_time=None, end_time=None, limit=None, offset=None, signature_id=None, signature_name=None, signature_type=None, site=None, sort_dir=None, sort_key=None, status=None):
        r"""ListSignatureDetailsRequest

        The model defined in huaweicloud sdk

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
        :param signature_id: 签名ID
        :type signature_id: str
        :param signature_name: 签名名称
        :type signature_name: str
        :param signature_type: 签名类型。支持枚举值： 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类
        :type signature_type: str
        :param site: 地域
        :type site: str
        :param sort_dir: 排序方式 1. desc：降序 2. asc：升序
        :type sort_dir: str
        :param sort_key: 排序字段
        :type sort_key: str
        :param status: 状态 1. PENDING_REVIEW：待签名审核 2. PROCESSING：内容审核通过，签名处理中 3. REVIEW_PASSED：处理完毕(待补充资质)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 4. REVIEW_NOT_PASS：审核不通过 5. TO_BE_ACTIVATED：待激活 6. PENDING_ACTIVATE：激活审核中 7. PENDING_QUALIFICATION_REVIEW：待资质审核，该状态下，用户不可发送短信 8. REAL_NAME_REGISTRATING：实名报备中，该状态下，用户不可发送短信 9. REVIEW_PASSED_QUALIFICATION_PROCESSING：处理完毕(资质审核中)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 10. REVIEW_PASSED_REAL_NAME_REGISTRATING：处理完毕(实名报备中)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 11. REVIEW_PASSED_REAL_NAME_REGISTRATE_FAIL：处理完毕(实名报备失败)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 12. REVIEW_PROCESSING_COMPLETED：处理完毕
        :type status: str
        """
        
        

        self._app_name = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._signature_id = None
        self._signature_name = None
        self._signature_type = None
        self._site = None
        self._sort_dir = None
        self._sort_key = None
        self._status = None
        self.discriminator = None

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
        if signature_id is not None:
            self.signature_id = signature_id
        if signature_name is not None:
            self.signature_name = signature_name
        if signature_type is not None:
            self.signature_type = signature_type
        if site is not None:
            self.site = site
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status

    @property
    def app_name(self):
        r"""Gets the app_name of this ListSignatureDetailsRequest.

        应用名称

        :return: The app_name of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListSignatureDetailsRequest.

        应用名称

        :param app_name: The app_name of this ListSignatureDetailsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSignatureDetailsRequest.

        开始时间

        :return: The start_time of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSignatureDetailsRequest.

        开始时间

        :param start_time: The start_time of this ListSignatureDetailsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSignatureDetailsRequest.

        结束时间

        :return: The end_time of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSignatureDetailsRequest.

        结束时间

        :param end_time: The end_time of this ListSignatureDetailsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListSignatureDetailsRequest.

        数量

        :return: The limit of this ListSignatureDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSignatureDetailsRequest.

        数量

        :param limit: The limit of this ListSignatureDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSignatureDetailsRequest.

        偏移量

        :return: The offset of this ListSignatureDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSignatureDetailsRequest.

        偏移量

        :param offset: The offset of this ListSignatureDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def signature_id(self):
        r"""Gets the signature_id of this ListSignatureDetailsRequest.

        签名ID

        :return: The signature_id of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        r"""Sets the signature_id of this ListSignatureDetailsRequest.

        签名ID

        :param signature_id: The signature_id of this ListSignatureDetailsRequest.
        :type signature_id: str
        """
        self._signature_id = signature_id

    @property
    def signature_name(self):
        r"""Gets the signature_name of this ListSignatureDetailsRequest.

        签名名称

        :return: The signature_name of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        r"""Sets the signature_name of this ListSignatureDetailsRequest.

        签名名称

        :param signature_name: The signature_name of this ListSignatureDetailsRequest.
        :type signature_name: str
        """
        self._signature_name = signature_name

    @property
    def signature_type(self):
        r"""Gets the signature_type of this ListSignatureDetailsRequest.

        签名类型。支持枚举值： 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类

        :return: The signature_type of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        r"""Sets the signature_type of this ListSignatureDetailsRequest.

        签名类型。支持枚举值： 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类

        :param signature_type: The signature_type of this ListSignatureDetailsRequest.
        :type signature_type: str
        """
        self._signature_type = signature_type

    @property
    def site(self):
        r"""Gets the site of this ListSignatureDetailsRequest.

        地域

        :return: The site of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        r"""Sets the site of this ListSignatureDetailsRequest.

        地域

        :param site: The site of this ListSignatureDetailsRequest.
        :type site: str
        """
        self._site = site

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListSignatureDetailsRequest.

        排序方式 1. desc：降序 2. asc：升序

        :return: The sort_dir of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListSignatureDetailsRequest.

        排序方式 1. desc：降序 2. asc：升序

        :param sort_dir: The sort_dir of this ListSignatureDetailsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListSignatureDetailsRequest.

        排序字段

        :return: The sort_key of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListSignatureDetailsRequest.

        排序字段

        :param sort_key: The sort_key of this ListSignatureDetailsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        r"""Gets the status of this ListSignatureDetailsRequest.

        状态 1. PENDING_REVIEW：待签名审核 2. PROCESSING：内容审核通过，签名处理中 3. REVIEW_PASSED：处理完毕(待补充资质)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 4. REVIEW_NOT_PASS：审核不通过 5. TO_BE_ACTIVATED：待激活 6. PENDING_ACTIVATE：激活审核中 7. PENDING_QUALIFICATION_REVIEW：待资质审核，该状态下，用户不可发送短信 8. REAL_NAME_REGISTRATING：实名报备中，该状态下，用户不可发送短信 9. REVIEW_PASSED_QUALIFICATION_PROCESSING：处理完毕(资质审核中)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 10. REVIEW_PASSED_REAL_NAME_REGISTRATING：处理完毕(实名报备中)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 11. REVIEW_PASSED_REAL_NAME_REGISTRATE_FAIL：处理完毕(实名报备失败)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 12. REVIEW_PROCESSING_COMPLETED：处理完毕

        :return: The status of this ListSignatureDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSignatureDetailsRequest.

        状态 1. PENDING_REVIEW：待签名审核 2. PROCESSING：内容审核通过，签名处理中 3. REVIEW_PASSED：处理完毕(待补充资质)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 4. REVIEW_NOT_PASS：审核不通过 5. TO_BE_ACTIVATED：待激活 6. PENDING_ACTIVATE：激活审核中 7. PENDING_QUALIFICATION_REVIEW：待资质审核，该状态下，用户不可发送短信 8. REAL_NAME_REGISTRATING：实名报备中，该状态下，用户不可发送短信 9. REVIEW_PASSED_QUALIFICATION_PROCESSING：处理完毕(资质审核中)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 10. REVIEW_PASSED_REAL_NAME_REGISTRATING：处理完毕(实名报备中)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 11. REVIEW_PASSED_REAL_NAME_REGISTRATE_FAIL：处理完毕(实名报备失败)，该状态仅针对存量签名补充资质有效。在该状态下，用户可发送短信，但发送短信可能会由于运营商资质管控而失败 12. REVIEW_PROCESSING_COMPLETED：处理完毕

        :param status: The status of this ListSignatureDetailsRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListSignatureDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
