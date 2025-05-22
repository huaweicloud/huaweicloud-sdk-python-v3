# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BucketSplitInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_dn_num': 'int',
        'after_scale_out_dn_num': 'int',
        'current_bucket_num': 'int',
        'after_scale_out_bucket_num': 'int',
        'is_bucket_split': 'bool',
        'bucket_tilt_rate': 'str',
        'after_scale_out_bucket_tilt_rate': 'str'
    }

    attribute_map = {
        'current_dn_num': 'current_dn_num',
        'after_scale_out_dn_num': 'after_scale_out_dn_num',
        'current_bucket_num': 'current_bucket_num',
        'after_scale_out_bucket_num': 'after_scale_out_bucket_num',
        'is_bucket_split': 'is_bucket_split',
        'bucket_tilt_rate': 'bucket_tilt_rate',
        'after_scale_out_bucket_tilt_rate': 'after_scale_out_bucket_tilt_rate'
    }

    def __init__(self, current_dn_num=None, after_scale_out_dn_num=None, current_bucket_num=None, after_scale_out_bucket_num=None, is_bucket_split=None, bucket_tilt_rate=None, after_scale_out_bucket_tilt_rate=None):
        r"""BucketSplitInfo

        The model defined in huaweicloud sdk

        :param current_dn_num: **参数解释**： 当前DN数。 **取值范围**： 不涉及。
        :type current_dn_num: int
        :param after_scale_out_dn_num: **参数解释**： 扩容后DN数。 **取值范围**： 不涉及。
        :type after_scale_out_dn_num: int
        :param current_bucket_num: **参数解释**： 当前bucket数。 **取值范围**： 不涉及。
        :type current_bucket_num: int
        :param after_scale_out_bucket_num: **参数解释**： 扩容后bucket数。 **取值范围**： 不涉及。
        :type after_scale_out_bucket_num: int
        :param is_bucket_split: **参数解释**： 扩容是否涉及bucket分裂。 **取值范围**： 不涉及。
        :type is_bucket_split: bool
        :param bucket_tilt_rate: **参数解释**： bucket DN倾斜率，用于衡量bucket在DN节点上不均衡程度。 **取值范围**： 不涉及。
        :type bucket_tilt_rate: str
        :param after_scale_out_bucket_tilt_rate: **参数解释**： 扩容后 bucket DN倾斜率，用于衡量扩容后bucket在DN节点上不均衡程度。 **取值范围**： 不涉及。
        :type after_scale_out_bucket_tilt_rate: str
        """
        
        

        self._current_dn_num = None
        self._after_scale_out_dn_num = None
        self._current_bucket_num = None
        self._after_scale_out_bucket_num = None
        self._is_bucket_split = None
        self._bucket_tilt_rate = None
        self._after_scale_out_bucket_tilt_rate = None
        self.discriminator = None

        if current_dn_num is not None:
            self.current_dn_num = current_dn_num
        if after_scale_out_dn_num is not None:
            self.after_scale_out_dn_num = after_scale_out_dn_num
        if current_bucket_num is not None:
            self.current_bucket_num = current_bucket_num
        if after_scale_out_bucket_num is not None:
            self.after_scale_out_bucket_num = after_scale_out_bucket_num
        if is_bucket_split is not None:
            self.is_bucket_split = is_bucket_split
        if bucket_tilt_rate is not None:
            self.bucket_tilt_rate = bucket_tilt_rate
        if after_scale_out_bucket_tilt_rate is not None:
            self.after_scale_out_bucket_tilt_rate = after_scale_out_bucket_tilt_rate

    @property
    def current_dn_num(self):
        r"""Gets the current_dn_num of this BucketSplitInfo.

        **参数解释**： 当前DN数。 **取值范围**： 不涉及。

        :return: The current_dn_num of this BucketSplitInfo.
        :rtype: int
        """
        return self._current_dn_num

    @current_dn_num.setter
    def current_dn_num(self, current_dn_num):
        r"""Sets the current_dn_num of this BucketSplitInfo.

        **参数解释**： 当前DN数。 **取值范围**： 不涉及。

        :param current_dn_num: The current_dn_num of this BucketSplitInfo.
        :type current_dn_num: int
        """
        self._current_dn_num = current_dn_num

    @property
    def after_scale_out_dn_num(self):
        r"""Gets the after_scale_out_dn_num of this BucketSplitInfo.

        **参数解释**： 扩容后DN数。 **取值范围**： 不涉及。

        :return: The after_scale_out_dn_num of this BucketSplitInfo.
        :rtype: int
        """
        return self._after_scale_out_dn_num

    @after_scale_out_dn_num.setter
    def after_scale_out_dn_num(self, after_scale_out_dn_num):
        r"""Sets the after_scale_out_dn_num of this BucketSplitInfo.

        **参数解释**： 扩容后DN数。 **取值范围**： 不涉及。

        :param after_scale_out_dn_num: The after_scale_out_dn_num of this BucketSplitInfo.
        :type after_scale_out_dn_num: int
        """
        self._after_scale_out_dn_num = after_scale_out_dn_num

    @property
    def current_bucket_num(self):
        r"""Gets the current_bucket_num of this BucketSplitInfo.

        **参数解释**： 当前bucket数。 **取值范围**： 不涉及。

        :return: The current_bucket_num of this BucketSplitInfo.
        :rtype: int
        """
        return self._current_bucket_num

    @current_bucket_num.setter
    def current_bucket_num(self, current_bucket_num):
        r"""Sets the current_bucket_num of this BucketSplitInfo.

        **参数解释**： 当前bucket数。 **取值范围**： 不涉及。

        :param current_bucket_num: The current_bucket_num of this BucketSplitInfo.
        :type current_bucket_num: int
        """
        self._current_bucket_num = current_bucket_num

    @property
    def after_scale_out_bucket_num(self):
        r"""Gets the after_scale_out_bucket_num of this BucketSplitInfo.

        **参数解释**： 扩容后bucket数。 **取值范围**： 不涉及。

        :return: The after_scale_out_bucket_num of this BucketSplitInfo.
        :rtype: int
        """
        return self._after_scale_out_bucket_num

    @after_scale_out_bucket_num.setter
    def after_scale_out_bucket_num(self, after_scale_out_bucket_num):
        r"""Sets the after_scale_out_bucket_num of this BucketSplitInfo.

        **参数解释**： 扩容后bucket数。 **取值范围**： 不涉及。

        :param after_scale_out_bucket_num: The after_scale_out_bucket_num of this BucketSplitInfo.
        :type after_scale_out_bucket_num: int
        """
        self._after_scale_out_bucket_num = after_scale_out_bucket_num

    @property
    def is_bucket_split(self):
        r"""Gets the is_bucket_split of this BucketSplitInfo.

        **参数解释**： 扩容是否涉及bucket分裂。 **取值范围**： 不涉及。

        :return: The is_bucket_split of this BucketSplitInfo.
        :rtype: bool
        """
        return self._is_bucket_split

    @is_bucket_split.setter
    def is_bucket_split(self, is_bucket_split):
        r"""Sets the is_bucket_split of this BucketSplitInfo.

        **参数解释**： 扩容是否涉及bucket分裂。 **取值范围**： 不涉及。

        :param is_bucket_split: The is_bucket_split of this BucketSplitInfo.
        :type is_bucket_split: bool
        """
        self._is_bucket_split = is_bucket_split

    @property
    def bucket_tilt_rate(self):
        r"""Gets the bucket_tilt_rate of this BucketSplitInfo.

        **参数解释**： bucket DN倾斜率，用于衡量bucket在DN节点上不均衡程度。 **取值范围**： 不涉及。

        :return: The bucket_tilt_rate of this BucketSplitInfo.
        :rtype: str
        """
        return self._bucket_tilt_rate

    @bucket_tilt_rate.setter
    def bucket_tilt_rate(self, bucket_tilt_rate):
        r"""Sets the bucket_tilt_rate of this BucketSplitInfo.

        **参数解释**： bucket DN倾斜率，用于衡量bucket在DN节点上不均衡程度。 **取值范围**： 不涉及。

        :param bucket_tilt_rate: The bucket_tilt_rate of this BucketSplitInfo.
        :type bucket_tilt_rate: str
        """
        self._bucket_tilt_rate = bucket_tilt_rate

    @property
    def after_scale_out_bucket_tilt_rate(self):
        r"""Gets the after_scale_out_bucket_tilt_rate of this BucketSplitInfo.

        **参数解释**： 扩容后 bucket DN倾斜率，用于衡量扩容后bucket在DN节点上不均衡程度。 **取值范围**： 不涉及。

        :return: The after_scale_out_bucket_tilt_rate of this BucketSplitInfo.
        :rtype: str
        """
        return self._after_scale_out_bucket_tilt_rate

    @after_scale_out_bucket_tilt_rate.setter
    def after_scale_out_bucket_tilt_rate(self, after_scale_out_bucket_tilt_rate):
        r"""Sets the after_scale_out_bucket_tilt_rate of this BucketSplitInfo.

        **参数解释**： 扩容后 bucket DN倾斜率，用于衡量扩容后bucket在DN节点上不均衡程度。 **取值范围**： 不涉及。

        :param after_scale_out_bucket_tilt_rate: The after_scale_out_bucket_tilt_rate of this BucketSplitInfo.
        :type after_scale_out_bucket_tilt_rate: str
        """
        self._after_scale_out_bucket_tilt_rate = after_scale_out_bucket_tilt_rate

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
        if not isinstance(other, BucketSplitInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
