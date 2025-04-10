# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLigandPreviewTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ligand_file': 'DrugFile',
        'preview_count': 'int',
        'count_limit': 'int',
        'generate_3d': 'bool'
    }

    attribute_map = {
        'ligand_file': 'ligand_file',
        'preview_count': 'preview_count',
        'count_limit': 'count_limit',
        'generate_3d': 'generate_3d'
    }

    def __init__(self, ligand_file=None, preview_count=None, count_limit=None, generate_3d=None):
        r"""CreateLigandPreviewTaskReq

        The model defined in huaweicloud sdk

        :param ligand_file: 
        :type ligand_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        :param preview_count: 预览数量，若分子数量大于预览数量，则超出预览数量部分只做计数
        :type preview_count: int
        :param count_limit: 计数上限，若分子数量大于计数上限，则终止计数并在结果中标明计数不完整（has_more&#x3D;true），计数数量应不小于preview_count
        :type count_limit: int
        :param generate_3d: 是否生成3D构象，默认为true
        :type generate_3d: bool
        """
        
        

        self._ligand_file = None
        self._preview_count = None
        self._count_limit = None
        self._generate_3d = None
        self.discriminator = None

        self.ligand_file = ligand_file
        if preview_count is not None:
            self.preview_count = preview_count
        if count_limit is not None:
            self.count_limit = count_limit
        if generate_3d is not None:
            self.generate_3d = generate_3d

    @property
    def ligand_file(self):
        r"""Gets the ligand_file of this CreateLigandPreviewTaskReq.

        :return: The ligand_file of this CreateLigandPreviewTaskReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._ligand_file

    @ligand_file.setter
    def ligand_file(self, ligand_file):
        r"""Sets the ligand_file of this CreateLigandPreviewTaskReq.

        :param ligand_file: The ligand_file of this CreateLigandPreviewTaskReq.
        :type ligand_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._ligand_file = ligand_file

    @property
    def preview_count(self):
        r"""Gets the preview_count of this CreateLigandPreviewTaskReq.

        预览数量，若分子数量大于预览数量，则超出预览数量部分只做计数

        :return: The preview_count of this CreateLigandPreviewTaskReq.
        :rtype: int
        """
        return self._preview_count

    @preview_count.setter
    def preview_count(self, preview_count):
        r"""Sets the preview_count of this CreateLigandPreviewTaskReq.

        预览数量，若分子数量大于预览数量，则超出预览数量部分只做计数

        :param preview_count: The preview_count of this CreateLigandPreviewTaskReq.
        :type preview_count: int
        """
        self._preview_count = preview_count

    @property
    def count_limit(self):
        r"""Gets the count_limit of this CreateLigandPreviewTaskReq.

        计数上限，若分子数量大于计数上限，则终止计数并在结果中标明计数不完整（has_more=true），计数数量应不小于preview_count

        :return: The count_limit of this CreateLigandPreviewTaskReq.
        :rtype: int
        """
        return self._count_limit

    @count_limit.setter
    def count_limit(self, count_limit):
        r"""Sets the count_limit of this CreateLigandPreviewTaskReq.

        计数上限，若分子数量大于计数上限，则终止计数并在结果中标明计数不完整（has_more=true），计数数量应不小于preview_count

        :param count_limit: The count_limit of this CreateLigandPreviewTaskReq.
        :type count_limit: int
        """
        self._count_limit = count_limit

    @property
    def generate_3d(self):
        r"""Gets the generate_3d of this CreateLigandPreviewTaskReq.

        是否生成3D构象，默认为true

        :return: The generate_3d of this CreateLigandPreviewTaskReq.
        :rtype: bool
        """
        return self._generate_3d

    @generate_3d.setter
    def generate_3d(self, generate_3d):
        r"""Sets the generate_3d of this CreateLigandPreviewTaskReq.

        是否生成3D构象，默认为true

        :param generate_3d: The generate_3d of this CreateLigandPreviewTaskReq.
        :type generate_3d: bool
        """
        self._generate_3d = generate_3d

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
        if not isinstance(other, CreateLigandPreviewTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
