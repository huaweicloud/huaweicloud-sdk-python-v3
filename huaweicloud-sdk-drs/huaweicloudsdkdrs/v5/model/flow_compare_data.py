# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowCompareData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'src_db': 'str',
        'src_tb': 'str',
        'dst_db': 'str',
        'dst_tb': 'str',
        'progress': 'int'
    }

    attribute_map = {
        'src_db': 'src_db',
        'src_tb': 'src_tb',
        'dst_db': 'dst_db',
        'dst_tb': 'dst_tb',
        'progress': 'progress'
    }

    def __init__(self, src_db=None, src_tb=None, dst_db=None, dst_tb=None, progress=None):
        """FlowCompareData

        The model defined in huaweicloud sdk

        :param src_db: 源数据库名称。
        :type src_db: str
        :param src_tb: 源对象名称。
        :type src_tb: str
        :param dst_db: 目标数据库名称。
        :type dst_db: str
        :param dst_tb: 目标对象名称。
        :type dst_tb: str
        :param progress: 进度，1-100。
        :type progress: int
        """
        
        

        self._src_db = None
        self._src_tb = None
        self._dst_db = None
        self._dst_tb = None
        self._progress = None
        self.discriminator = None

        if src_db is not None:
            self.src_db = src_db
        if src_tb is not None:
            self.src_tb = src_tb
        if dst_db is not None:
            self.dst_db = dst_db
        if dst_tb is not None:
            self.dst_tb = dst_tb
        if progress is not None:
            self.progress = progress

    @property
    def src_db(self):
        """Gets the src_db of this FlowCompareData.

        源数据库名称。

        :return: The src_db of this FlowCompareData.
        :rtype: str
        """
        return self._src_db

    @src_db.setter
    def src_db(self, src_db):
        """Sets the src_db of this FlowCompareData.

        源数据库名称。

        :param src_db: The src_db of this FlowCompareData.
        :type src_db: str
        """
        self._src_db = src_db

    @property
    def src_tb(self):
        """Gets the src_tb of this FlowCompareData.

        源对象名称。

        :return: The src_tb of this FlowCompareData.
        :rtype: str
        """
        return self._src_tb

    @src_tb.setter
    def src_tb(self, src_tb):
        """Sets the src_tb of this FlowCompareData.

        源对象名称。

        :param src_tb: The src_tb of this FlowCompareData.
        :type src_tb: str
        """
        self._src_tb = src_tb

    @property
    def dst_db(self):
        """Gets the dst_db of this FlowCompareData.

        目标数据库名称。

        :return: The dst_db of this FlowCompareData.
        :rtype: str
        """
        return self._dst_db

    @dst_db.setter
    def dst_db(self, dst_db):
        """Sets the dst_db of this FlowCompareData.

        目标数据库名称。

        :param dst_db: The dst_db of this FlowCompareData.
        :type dst_db: str
        """
        self._dst_db = dst_db

    @property
    def dst_tb(self):
        """Gets the dst_tb of this FlowCompareData.

        目标对象名称。

        :return: The dst_tb of this FlowCompareData.
        :rtype: str
        """
        return self._dst_tb

    @dst_tb.setter
    def dst_tb(self, dst_tb):
        """Sets the dst_tb of this FlowCompareData.

        目标对象名称。

        :param dst_tb: The dst_tb of this FlowCompareData.
        :type dst_tb: str
        """
        self._dst_tb = dst_tb

    @property
    def progress(self):
        """Gets the progress of this FlowCompareData.

        进度，1-100。

        :return: The progress of this FlowCompareData.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this FlowCompareData.

        进度，1-100。

        :param progress: The progress of this FlowCompareData.
        :type progress: int
        """
        self._progress = progress

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
        if not isinstance(other, FlowCompareData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
