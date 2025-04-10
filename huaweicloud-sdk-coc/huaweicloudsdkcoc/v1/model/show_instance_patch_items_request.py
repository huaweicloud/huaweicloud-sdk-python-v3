# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstancePatchItemsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_compliant_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'title': 'str',
        'sort_dir': 'str',
        'sort_key': 'str',
        'patch_status': 'str',
        'classification': 'str',
        'severity_level': 'str',
        'compliance_level': 'str'
    }

    attribute_map = {
        'instance_compliant_id': 'instance_compliant_id',
        'offset': 'offset',
        'limit': 'limit',
        'title': 'title',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'patch_status': 'patch_status',
        'classification': 'classification',
        'severity_level': 'severity_level',
        'compliance_level': 'compliance_level'
    }

    def __init__(self, instance_compliant_id=None, offset=None, limit=None, title=None, sort_dir=None, sort_key=None, patch_status=None, classification=None, severity_level=None, compliance_level=None):
        r"""ShowInstancePatchItemsRequest

        The model defined in huaweicloud sdk

        :param instance_compliant_id: 合规性报告id
        :type instance_compliant_id: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页数量
        :type limit: int
        :param title: 补丁名称
        :type title: str
        :param sort_dir: 排序 - asc：升序 - desc：降序
        :type sort_dir: str
        :param sort_key: 排序字段 -installed_time：补丁安装时间
        :type sort_key: str
        :param patch_status: 补丁状态 INSTALLED：已安装 INSTALLED_OTHER：已安装其他 MISSING：缺失 REJECT：拒绝 FAILED：失败 PENDING_REBOOT：已安装待重启
        :type patch_status: str
        :param classification: 分类
        :type classification: str
        :param severity_level: 严重性级别
        :type severity_level: str
        :param compliance_level: 合规性级别
        :type compliance_level: str
        """
        
        

        self._instance_compliant_id = None
        self._offset = None
        self._limit = None
        self._title = None
        self._sort_dir = None
        self._sort_key = None
        self._patch_status = None
        self._classification = None
        self._severity_level = None
        self._compliance_level = None
        self.discriminator = None

        self.instance_compliant_id = instance_compliant_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if title is not None:
            self.title = title
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if patch_status is not None:
            self.patch_status = patch_status
        if classification is not None:
            self.classification = classification
        if severity_level is not None:
            self.severity_level = severity_level
        if compliance_level is not None:
            self.compliance_level = compliance_level

    @property
    def instance_compliant_id(self):
        r"""Gets the instance_compliant_id of this ShowInstancePatchItemsRequest.

        合规性报告id

        :return: The instance_compliant_id of this ShowInstancePatchItemsRequest.
        :rtype: str
        """
        return self._instance_compliant_id

    @instance_compliant_id.setter
    def instance_compliant_id(self, instance_compliant_id):
        r"""Sets the instance_compliant_id of this ShowInstancePatchItemsRequest.

        合规性报告id

        :param instance_compliant_id: The instance_compliant_id of this ShowInstancePatchItemsRequest.
        :type instance_compliant_id: str
        """
        self._instance_compliant_id = instance_compliant_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowInstancePatchItemsRequest.

        偏移量

        :return: The offset of this ShowInstancePatchItemsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowInstancePatchItemsRequest.

        偏移量

        :param offset: The offset of this ShowInstancePatchItemsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstancePatchItemsRequest.

        每页数量

        :return: The limit of this ShowInstancePatchItemsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstancePatchItemsRequest.

        每页数量

        :param limit: The limit of this ShowInstancePatchItemsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def title(self):
        r"""Gets the title of this ShowInstancePatchItemsRequest.

        补丁名称

        :return: The title of this ShowInstancePatchItemsRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowInstancePatchItemsRequest.

        补丁名称

        :param title: The title of this ShowInstancePatchItemsRequest.
        :type title: str
        """
        self._title = title

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ShowInstancePatchItemsRequest.

        排序 - asc：升序 - desc：降序

        :return: The sort_dir of this ShowInstancePatchItemsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ShowInstancePatchItemsRequest.

        排序 - asc：升序 - desc：降序

        :param sort_dir: The sort_dir of this ShowInstancePatchItemsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ShowInstancePatchItemsRequest.

        排序字段 -installed_time：补丁安装时间

        :return: The sort_key of this ShowInstancePatchItemsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ShowInstancePatchItemsRequest.

        排序字段 -installed_time：补丁安装时间

        :param sort_key: The sort_key of this ShowInstancePatchItemsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def patch_status(self):
        r"""Gets the patch_status of this ShowInstancePatchItemsRequest.

        补丁状态 INSTALLED：已安装 INSTALLED_OTHER：已安装其他 MISSING：缺失 REJECT：拒绝 FAILED：失败 PENDING_REBOOT：已安装待重启

        :return: The patch_status of this ShowInstancePatchItemsRequest.
        :rtype: str
        """
        return self._patch_status

    @patch_status.setter
    def patch_status(self, patch_status):
        r"""Sets the patch_status of this ShowInstancePatchItemsRequest.

        补丁状态 INSTALLED：已安装 INSTALLED_OTHER：已安装其他 MISSING：缺失 REJECT：拒绝 FAILED：失败 PENDING_REBOOT：已安装待重启

        :param patch_status: The patch_status of this ShowInstancePatchItemsRequest.
        :type patch_status: str
        """
        self._patch_status = patch_status

    @property
    def classification(self):
        r"""Gets the classification of this ShowInstancePatchItemsRequest.

        分类

        :return: The classification of this ShowInstancePatchItemsRequest.
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        r"""Sets the classification of this ShowInstancePatchItemsRequest.

        分类

        :param classification: The classification of this ShowInstancePatchItemsRequest.
        :type classification: str
        """
        self._classification = classification

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ShowInstancePatchItemsRequest.

        严重性级别

        :return: The severity_level of this ShowInstancePatchItemsRequest.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ShowInstancePatchItemsRequest.

        严重性级别

        :param severity_level: The severity_level of this ShowInstancePatchItemsRequest.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def compliance_level(self):
        r"""Gets the compliance_level of this ShowInstancePatchItemsRequest.

        合规性级别

        :return: The compliance_level of this ShowInstancePatchItemsRequest.
        :rtype: str
        """
        return self._compliance_level

    @compliance_level.setter
    def compliance_level(self, compliance_level):
        r"""Sets the compliance_level of this ShowInstancePatchItemsRequest.

        合规性级别

        :param compliance_level: The compliance_level of this ShowInstancePatchItemsRequest.
        :type compliance_level: str
        """
        self._compliance_level = compliance_level

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
        if not isinstance(other, ShowInstancePatchItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
